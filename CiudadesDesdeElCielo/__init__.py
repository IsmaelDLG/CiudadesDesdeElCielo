import os
import glob
import xml.etree.ElementTree as ET

# GLOBAL VARS
XML_PATH = os.path.dirname(__file__) + '/Images/Training/Anno/'
IMG_PATH = os.path.dirname(__file__) + '/Images/Training/Img/'

# Do for all xml files
for file in os.listdir(XML_PATH):
	tree = ET.parse(XML_PATH + file)
	element = tree.getroot().find('path')
	# Changes path to dir + filename
	element.text = IMG_PATH + glob.glob(IMG_PATH + file.split("/")[-1].split(".")[0] + ".*")[0]
	# Writes new xml path to file
	tree.write(XML_PATH + file)
