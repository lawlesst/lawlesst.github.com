Title:Solr Document Signatures
Date:03-29-13
Slug:solr-etags

I previously [wrote](http://lawlesst.github.com/notebook/vivo-caching.html) about working with Apache [mod_cache](http://httpd.apache.org/docs/2.2/caching.html), HTTP [ETags](http://en.wikipedia.org/wiki/HTTP_ETag), and [VIVO](http://www.vivoweb.org/) to cache public pages.  After writing that post, I found that [Solr supports adding "signatures" to documents](http://wiki.apache.org/solr/Deduplication) as a way to identify if a document is identical to another.  This [feature](http://wiki.apache.org/solr/Deduplication) was added to Solr as a way to identify duplicate documents or prevent duplicates documents from being added to the index.  However it is flexible enough to meet the needs for my intended use, which is to generate a unique identifying string for the contents of a Solr document and use that string within a web application to validate [ETags](http://en.wikipedia.org/wiki/HTTP_ETag) forwarded by clients.  

This feature is nicely documented on the Solr wiki under [Deduplication](http://wiki.apache.org/solr/Deduplication).  The exact changes I made are listed below.  For my application, using this built-in updateRequestProcessor eliminates the need to generate hashes as part of the indexing code or on the fly in cache validation logic.  

### Solr configuration 

####solrconfig.xml

 * Add the update request processor to the UpdateRequest chain.

~~~~~{.xml}

<updateRequestProcessorChain name="etag">
     <processor class="solr.processor.SignatureUpdateProcessorFactory">
       <bool name="enabled">true</bool>
       <str name="signatureField">etag</str>
       <!-- For VIVO we don't want to overwrite duplicates if we 
       somehow come across one.
       -->
       <bool name="overwriteDupes">false</bool>
       <!-- using the Lookup3Signature since the documentation says it is faster
       and we should not encounter actual duplicates in a VIVO Solr index since we
       are including the URI in the Solr document. -->
       <str name="signatureClass">solr.processor.Lookup3Signature</str>
     </processor>
     <processor class="solr.LogUpdateProcessorFactory" />
     <processor class="solr.RunUpdateProcessorFactory" />
   </updateRequestProcessorChain>

~~~~~

  * Add the update chain to the update request handler so that it is called after each document is updated.  

~~~~~{.xml}
  <requestHandler name="/update" 
                  class="solr.XmlUpdateRequestHandler">
       <lst name="defaults">
         <str name="update.processor">etag</str>
       </lst>
    </requestHandler>

~~~~~

####schema.xml

* Add the field to store the signature to the index.

~~~~~{.xml}
<!-- In this case we want to store it for retrieval by our web application 
    so stored=true.  We won't be searching on this field and won't be using it
    to automatically overwrite duplicates so indexed=false. -->
<field name="etag" type="string" stored="true" indexed="false" multiValued="false" />

~~~~~

After making these adjustments, restarting Solr and re-indexing your content, you should see a new field in the Solr documents called 'etag' and its content should be a hash of its contents.  

Solr also has [built in support for ETags and caching in general](http://wiki.apache.org/solr/SolrAndHTTPCaches), but I don't think this is quite what I want in this situation.  
