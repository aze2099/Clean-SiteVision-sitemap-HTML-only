import codecs
import chardet
import sys
from lxml import etree as ET
from datetime import date
import os

input_file_path = sys.argv[1]

# Först kontrollerar vi filens kodning
with open(input_file_path, 'rb') as f:
    result = chardet.detect(f.read())  # eller readline om filen är stor

# Sedan öppnar vi filen med den upptäckta kodningen
parser = ET.XMLParser(recover=True, encoding=result['encoding'])

with codecs.open(input_file_path, 'r', encoding=result['encoding'], errors='ignore') as f:
    tree = ET.parse(f, parser)

root = tree.getroot()

# Samla alla url-element
ns = {'ns0': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
url_elements = root.findall('.//ns0:url', ns)

# Filtrera url-element med endast .html webbsidor (lägg till fler ändelser vid behov)
webpage_elements = [url for url in url_elements if url.find('ns0:loc', ns).text.endswith('.html')]

print(f"Hittade {len(webpage_elements)} .html webbsidor")

# Skapa ny sitemap-fil med endast webbsidor
new_root = ET.Element('urlset', {
    ET.QName('xmlns'): "http://www.sitemaps.org/schemas/sitemap/0.9", 
    ET.QName('xmlns', 'xsi'): "http://www.w3.org/2001/XMLSchema-instance", 
    ET.QName('xsi', 'schemaLocation'): "http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"})

for elem in webpage_elements:
    new_elem = ET.SubElement(new_root, 'url')
    for child in elem:
        new_child = ET.SubElement(new_elem, child.tag.split('}')[-1])
        new_child.text = child.text
        if child.attrib:
            new_child.attrib.update(child.attrib)

new_tree = ET.ElementTree(new_root)

if len(new_root):
    print("Den nya sitemap har innehåll")
else:
    print("Den nya sitemap är tom")

# Genererar ett unikt output-filnamn baserat på dagens datum och ser till att det inte finns några dubletter
today = date.today()
output_file_path = f"clean_sitemap_{today.isoformat()}.xml"
counter = 1

while os.path.exists(output_file_path):
    output_file_path = f"clean_sitemap_{today.isoformat()}_{counter}.xml"
    counter += 1

# Spara den nya sitemap-filen
new_tree.write(output_file_path, encoding='utf-8', xml_declaration=True, pretty_print=True)

print(f"Sitemap sparad till: {output_file_path}")
