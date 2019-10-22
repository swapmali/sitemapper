from xml.dom import minidom
import os
# parse an xml file by name
mydoc = minidom.parse('sitemap.xml')

items = mydoc.getElementsByTagName('loc')
fp = open("sitemap_links.txt", "w+")
print(items)
# all items data

print('\nAll item data:')
for elem in items:
    fp.write(elem.firstChild.data+"\n")
    print(elem.firstChild.data)
print("\n Data Written to a file sitemap_links.txt")
fp.close()
