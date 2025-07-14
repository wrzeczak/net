print(f"#{'-'*80}#")
print("# WRZ: Article Generator")

output_filename = input("Output filename?: ")
ARTICLE_TITLE = input("Article title?: ")
ARTICLE_SUBTITLE = input("Article subtitle?: ")
ARTICLE_DATE = input("Article date (DD Month YEAR)?: ")

article = f"""<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta content="{ARTICLE_TITLE} - wrzeczak.net" property="og:title"/>
    <meta content="'{ARTICLE_SUBTITLE}' Written {ARTICLE_DATE}." property="og:description"/>
    <meta content="#bddabe" data-react-helmet="true" name="theme-color" />
    
    <link rel="stylesheet" href="https://wrzeczak.net/styles.css">
    <!-- TODO: <link rel="icon" href="res/favicon.ico"> -->

    <title>{ARTICLE_TITLE}</title>
</head>
<body>
    <!-- Header -->
    <div id="title">
        <a id="clickable" style="text-decoration: none; color: var(--txt-color);" href="https://wrzeczak.net/index.html">{ARTICLE_TITLE}</a> 
        <div id="subtitle">
            {ARTICLE_SUBTITLE}
        </div>
    </div>

    <!-- Article Sidebar -->
    <div id="sidebar">
        Written {ARTICLE_DATE}.<br/><br/>
        <div id="clickable" id="sb-title">
            <a href="https://wrzeczak.net/articles/index.html">Return to All Articles</a>
        </div>
    </div>

    <!-- Central Aritcle View -->
    <div id="article">
        
   </div>

    <!--
    <footer id="sb-aligned">
        <div style="text-align:center">
            <a href="https://cedars.xyz/">return to the forest</a><br/>
            <a href="https://cedars.xyz/previous">< prev</a>
            <a href="https://cedars.xyz/next">next ></a><br/>
            <a href="https://cedars.xyz/random">https://randint(0, 255).xyz</a>
        </div>
    </footer>
    -->
</body>
</html>
"""

with open(output_filename, "w") as f:
    print(article, file=f)

print(f"\n# Article output to {output_filename}.")
print(f"#{'-'*80}#")
