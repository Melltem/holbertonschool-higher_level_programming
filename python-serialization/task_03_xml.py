#!/usr/bin/env python3
"""Serialize and deserialize with XML"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize and deserialize with XML"""
    try:
        root = ET.Element("data")

        for key in dictionary:
            item = ET.SubElement(root, key)
            item.text = str(dictionary[key]


        tree = ET.ElementTree(root)
        tree.write(filename)

        return True
    except:
        return False
def deserialize_from_xml(filename):
    """Serialize and deserialize with XML"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for item in root:
            result[item.tag] = item.text

        return result
    except:
        return None
