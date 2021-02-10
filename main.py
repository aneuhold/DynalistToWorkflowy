from src.printFunctions import *
import xml.etree.ElementTree as ET
from os import path

opmlFileName = './Main.opml'

tree = ET.parse('./Main.opml')
root = tree.getroot()
for outline in root.iter('outline'):
  text = outline.attrib['text']
  print(text)
