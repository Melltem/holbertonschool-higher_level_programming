import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")
        for key in dictionary:
            item = ET.SubElement(root, key)
            item.text = str(dictionary[key])
        tree = ET.ElementTree(root)
        tree.write(filename)
