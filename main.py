from src.printFunctions import *
import xml.etree.ElementTree as ET
from os import path
import re
from src.conversion import convertDates

opmlFileName = './Main.opml'

tree = ET.parse('./Main.opml')
root = tree.getroot()
convertDates('If they really need to pay early then according to Amr !(2020-12-22) , Amr can setup a manual invoice thr !(2020-12-22)')

'''
for outline in root.iter('outline'):
  text = outline.attrib['text']
  convertDates(text)
'''
