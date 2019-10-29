import glob
import pandas as pd
from pathlib import Path
import re

def generateArray(file):
    with open(file, "r") as f:
        arr = lista = f.read().splitlines()

def returnEllipseListFiles(path):
    return [str(f) for f in  Path(path).glob("**/*-ellipseList.txt") ]

folder = glob.glob("dataset/*.jpg")
folder = pd.Series(folder)
files = returnEllipseListFiles("labels")

#vamos a crear diccionarios usando regex
#regex que nos distingue los diferentes caracteres 
# de cada archivo de la dataset (de las fotos) (\d)*_(\d)*_(\d)*_big_img_(\d)*
#{'name: ': , 'annotations ': []}

print(files)