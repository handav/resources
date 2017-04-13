import os
import csv
import urllib
import shutil
import requests

csvfolder = './agg'
imagefolder = './images/'
counter = {}

def getUrls(filepath):
    with open(filepath, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            emotion = row[0]
            url = row[1]
            no = int(row[2])
            yes = int(row[3])
            saveto = imagefolder + emotion + '/'
            if yes > 3:
                downloadPhoto(url, saveto, emotion)


def downloadPhoto(url, filepath, emotion):
    if (os.path.isdir(filepath) == False):
        print 'no folder called '+filepath
        os.makedirs(filepath)

    if emotion not in counter:
        counter[emotion] = 0

    response = requests.get(url, stream=True)
    filename = filepath + str(counter[emotion])
    if not (os.path.exists(filename)):
        print 'saving '+filename
        with open(filename, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
    else:
        print filename + ' already exists'
    counter[emotion]+=1



for filename in os.listdir(csvfolder):
    if filename.endswith(".csv") and 'amusement' not in filename and 'anger' not in filename and 'awe' not in filename and 'contentment' not in filename and 'disgust' not in filename and 'excitement' not in filename and 'fear' not in filename: 
        getUrls(os.path.join(csvfolder, filename))
        continue
    else:
        continue   


