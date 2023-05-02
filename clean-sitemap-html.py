from lxml import etree as ET

#Börja med att ladda ned och packa upp Sitevisions sitemap-fil. Den är packad i formatet .gz.

# Ladda sitemap-filen
file_path = r'C:\Temp\Shared\sitemap1.xml'

# Skapa en parser med 'recover=True'-parametern för att hantera eventuella syntaxfel
parser = ET.XMLParser(recover=True)

# Använd den skapade parsern när du parsa XML-filen
tree = ET.parse(file_path, parser)

root = tree.getroot()

# Samla alla url-element
ns = {'ns0': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
url_elements = root.findall('.//ns0:url', ns)

# Filtrera url-element med endast .html webbsidor (lägg till fler ändelser vid behov)
webpage_elements = [url for url in url_elements if url.find('ns0:loc', ns).text.endswith('.html')]

print(f"Found {len(webpage_elements)} .html webpages")

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
    print("New sitemap has content")
else:
    print("New sitemap is empty")

# Spara den nya sitemap-filen
output_file_path = r'C:\Temp\Shared\clean_sitemap.xml'
new_tree.write(output_file_path, encoding='utf-8', xml_declaration=True, pretty_print=True)
