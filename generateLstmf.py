import os
import subprocess

#Config
dir = "tesstrain/data/comismsh-ground-truth"
imageExt = 'jpg'

#Check if Directory exists
if not os.path.exists(dir):
    print("Folder not found: %s" % (dir))
    exit

#Get all files in that directory
files = os.listdir(dir)
validNames = []

#Get names that has both image & box exists
for file in files:
    if file.endswith('.' + imageExt):
        name = os.path.basename(file).split('.')[0]
        if os.path.exists(dir + '/' + name + '.box'):
            validNames.append(name)

#foreach name run > tesseract name.jpg name lstm.train
for name in validNames:
    subprocess.run([
        'tesseract',
        f'{name}.{imageExt}',
        name,
        'lstm.train'
    ], cwd= dir)

print('Done.')