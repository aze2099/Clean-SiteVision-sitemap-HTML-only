# Clean-SiteVision-sitemap-HTML-only

Städar Sitevisions sitemap-fil från allt som inte är html. (går lätt att lägga till fler filändelser om man vill det)

# Börja här
Börja med att ladda ned och packa upp Sitevisions sitemap-fil. Den är packad i formatet .gz.

# Ändra i skriptet
Ändra därefter sökvägen i skriptet till var du sparat den uppackade filen: 

"file_path = r'C:\Temp\Shared\sitemap1.xml'"

och vad du vill få för utfil:

"output_file_path = r'C:\Temp\Shared\clean_sitemap.xml'"

# Mål
Målet med detta skript är att kunna köra samtliga sidor på en sitevisionwebbplats med Webperf Core. 
För att göra detta behöver du sedan ladda upp filen på nätet igen för att Webperf Core ska få en URL att köra mot.
