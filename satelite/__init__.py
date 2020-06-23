"""
import os
import glob
from pathlib import Path
import xml.etree.ElementTree as ET

# GLOBAL VARS
TRAIN_PATH = (
    os.path.dirname(os.path.abspath(__file__))
    + os.path.sep
    + os.path.join("Tensorflow", "workspace", "images", "train")
    + os.path.sep
)

# Do for all xml files
for file in os.listdir(TRAIN_PATH):
    if file.endswith(".xml"):
        tree = ET.parse(TRAIN_PATH + file)
        element = tree.getroot().find("path")
        # Changes path to dir + filename
        element.text = (
            glob.glob(TRAIN_PATH + file.split("/")[-1].split(".")[0] + ".*")[0]
        )
        # Writes new xml path to file
        tree.write(TRAIN_PATH + file)
"""