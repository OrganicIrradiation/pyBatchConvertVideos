import os
import time
import subprocess
import sys
 
fileList = []
rootdir = raw_input("Root Dir: ")
for root, subFolders, files in os.walk(rootdir):
    for file in files:
        theFile = os.path.join(root,file)
        fileName, fileExtension = os.path.splitext(theFile)
        if fileExtension.lower() in ('.avi', '.divx', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv'):
            print 'Adding',theFile
            fileList.append(theFile)
 
runstr = '"C:\Program Files\Handbrake\HandBrakeCLI.exe" -i "{0}" -o "{1}" --preset="Normal" --two-pass --turbo'

print '=======--------======='

while fileList:
    inFile = fileList.pop()
    fileName, fileExtension = os.path.splitext(inFile)
    outFile = fileName+'.mp4'
 
    print 'Processing',inFile
    returncode  = subprocess.call(runstr.format(inFile,outFile))
    time.sleep(5)
    print 'Removing',inFile
    os.remove(inFile)
