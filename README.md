# Clean-SiteVision-sitemap-HTML-only
Städar Sitevisions sitemap-fil från allt som inte är html. (Det går lätt att lägga till fler eller byta filändelser om man vill det under ".text.endswith('.html')" i skriptet)

# Börja här
Börja med att ladda ned och packa upp Sitevisions sitemap-fil. Den är packad i formatet .gz. (Packas upp med "gunzip" till exempel). Du hittar sitemapfilen sannolikt på www.dindomän.se/sitemap1.xml.gz. Om du inte hittar den där så kolla www.dindomän.se/sitemap.xml, den adressen har en hänvisning till din riktiga sitemapfil.

# Installera
Ett moment i skriptet är att laga om det finns felaktiga tecken i filen. För att detta ska göras behöver först tillägget Chardet installeras med "pip install chardet".

# Kör
I terminalfönstret kör skriptet med "python clean-sitemap-html.py [sökväg]filnamn.xml". Den genererar en utdatatfil som heter "clean_sitemap_[datum].xml".

# Mål
Målet med detta skript är att kunna köra samtliga sidor på en sitevisionwebbplats med Webperf Core. Detta utan att testet ska köra mot PDF:er, bilder eller andra irrelevanta filer.
För att göra detta behöver du sedan ladda upp sitemap-filen på nätet igen för att Webperf Core ska få en URL att köra mot.
