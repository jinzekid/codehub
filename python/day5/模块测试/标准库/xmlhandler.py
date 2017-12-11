# Author: Jason Lu

import xml.etree.cElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()
print(root.tag)

# 遍历xml
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag, i.text, i.attrib)

# 只遍历year的值
for node in root.iter("year"):
    print(node.tag, node.text)

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated", "yes")

tree.write("xmltest.xml")

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')





