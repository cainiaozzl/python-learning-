#!/usr/bin/env python3
import zipfile,os
def backupToZip(folder):
    #Backup the entire contents of "folder" into a Zip file.

    folder = os.path.abspath(folder) #make sure folder is absolute

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    #create the zip file:
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    #Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
    #Add all the files in this folder to the ZIP file.
    for filename in filenames:
        newBase = os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue #don't backup the backuozip files
    backupZip.close()
    print('Done')
backupToZip('/home/zzl/PycharmProjects')


