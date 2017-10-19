from lxml import etree
import requests
import io

data = requests.get("https://www.vandenborre.be/lcd-led-tv/proline-l3237hd").text

parser = etree.HTMLParser()
tree = etree.parse(io.StringIO(data), parser)

print(tree.get_element_by_id("prodHeaderInfo").text_content())

#print(etree.tostring(root, pretty_print=True).decode("utf-8"))
