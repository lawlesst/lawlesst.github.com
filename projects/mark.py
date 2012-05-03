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
   <script type="text/javascript">

      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-2790298-5']);
      _gaq.push(['_trackPageview']);

      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();

    </script>
   </head>
   <body>
   <h1> Ted Lawless -- Projects</h1>
   <div id="main">
"""
txt = open(sys.argv[1], 'r')
txt = txt.read()
footer = """
	</div>
   </body>
 </html>
"""
html = markdown.markdown(unicode(txt, errors='ignore'), extensions=['toc'])
print header + html + footer


   


