import os
import re
import shutil
from zipfile import ZipFile

def main():
    # Add all files in downloads to a list.
    zip_files = []
    for root, dirs, files in os.walk('C:/Users/bs404/Downloads'):
        for filename in files:
            zip_files.append(filename)
    
    # Remove files that aren't zip files.
    zip_files = ['C:/Users/bs404/Downloads/' + zf for zf in zip_files if re.match('^.+\.zip$', zf)]

    # Extract the zip files.
    folders = []
    for zf in zip_files:
        with ZipFile(zf, 'r') as zipObj:
            # Remove .zip ending.
            folder = zf[:-4]
            # Place contents in folder w/ title of the zip file.
            zipObj.extractall(folder)
            folders.append(folder)

    # Move each song folder to CustomLevels folder.
    dest = 'D:/Oculus/Software/hyperbolic-magnetism-beat-saber/Beat Saber_Data/CustomLevels'
    for folder in folders:
        shutil.move(folder, dest)
        os.remove(folder + '.zip')

if __name__ == '__main__':
    main()