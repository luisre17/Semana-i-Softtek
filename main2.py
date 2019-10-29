import glob
from pathlib import Path
import pandas as pd
import re
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import matplotlib.patches as patches
import numpy as np 
import os

def generateArray(file):
    with open(file, "r") as f:
        arr = f.read().splitlines() 
    arr_len = len(arr)
    i = 0    
    # regex (version reducica, es menos pesado para la compu)
    rg = re.compile("(\d)*_(\d)*_(\d)*_big")
    output = []
    while i != arr_len:
    	val = arr[i] #nombre de la imagen
    	mtch = rg.match(val)
    	if mtch:
    		#el try except ayuda a diferenciar si tienen imagen o no 
    		try:
    			di = dict() #el diccionario 
    			val = "{}.jpg".format(val)
    			di["name"] = val
    			#matplotlib
    			img = mpimg.imread(os.path.join("dataset", val))
    			#height, width, RGB 
    			(h, w, _) = img.shape

    			jumps = int(arr[i+1])
    			temp = []
    			for j in range(0, jumps):
    				coords = arr[i + j +2]
    				temp.append(coords)
    			di["annotations"] = temp
    		except:
    			#algoo
    			print("{} not found....".format(val))
    			i+=1
    	else:
    		i+=1

def returnElllipseListFiles(path):
    return [str(f) for f in Path(path).glob('**/*-ellipseList.txt')]

folder = glob.glob("dataset/*.jpg")
folder = pd.Series(folder)
files = returnElllipseListFiles("labels")
