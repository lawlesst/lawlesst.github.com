import markdown, sys
header = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
 <head>
 <META http-equiv="Content-Type" content="text/html; charset=utf-8">
 <META name="Author" content="Ted Lawless">
     <title>
       Ted Lawless
     </title>
	 <link rel="stylesheet" type="text/css" href="style.css">
   </head>
   <body>
   <h1> Ted Lawless -- Projects</h1>
   <div id="main">
"""
txt = open(sys.argv[1], 'r')
txt = txt.read()
footer = """
	</div>
        <script type="text/javascript">
        var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
        document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
        </script>
        <script type="text/javascript">
        try {
            var pageTracker = _gat._getTracker("UA-2790298-4");
            pageTracker._trackPageview();
        } catch(err) {}</script>
   </body>
 </html>
"""
html = markdown.markdown(unicode(txt, errors='ignore'), extensions=['toc'])
print header + html + footer


   


