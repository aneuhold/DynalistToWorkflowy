from src.printFunctions import *
import xml.etree.ElementTree as ET
from os import path
import re
from src.dateConversion import convertDates
from src.linkConversion import convertLinks

opmlFileName = './Main.opml'

tree = ET.parse(opmlFileName)
root = tree.getroot()
testString = 'If they really need to pay early then according to Amr !(2020-12-22) , Amr can setup a manual invoice thr !(2020-12-22)'

for outline in root.iter('outline'):
  text = outline.attrib['text']
  outline.attrib['text'] = convertDates(text)
  outline.attrib['text'] = convertLinks(outline.attrib['text'])

  # Convert to workflowy type of complete attribute 😛
  if 'complete' in outline.attrib:
    outline.attrib['_complete'] = outline.attrib['complete']

tree.write('outpute-text.opml')
