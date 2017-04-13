import os
import csv
import urllib
import shutil
import requests

csvfolder = './data'
imagefolder = './images/'

def getUrls(filepath):
    with open(filepath, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            #change name to whatever you want it
            name = row[0]
            #make sure url is the correct row, row[1] refers to a specific dataset
            url = row[40]
            print url
            #if you want to put them in different folders, add that after 'imagefolder'
            if 'metmuseum' in url:
                saveto = imagefolder
                downloadPhoto(url, saveto, name)


def downloadPhoto(url, filepath, name):
    if (os.path.isdir(filepath) == False):
        print 'no folder called '+filepath
        os.makedirs(filepath)

    response = requests.get(url, stream=True)
    filename = filepath + name
    if not (os.path.exists(filename)):
        print 'saving '+filename
        with open(filename, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
    else:
        print filename + ' already exists'


for filename in os.listdir(csvfolder):
    if filename.endswith(".csv"): 
        getUrls(os.path.join(csvfolder, filename))
        continue
    else:
        continue   


