import os
import re
from zipfile import ZipFile

# See if a zip file matches the format of a song file
def is_a_song(f):
    if re.match("^[0-9]+.zip$", f):
        return True
    else:
        return False

# Add all zip files to a list
zip_files = []
for root, dirs, files in os.walk("."):
    for filename in files:
        zip_files.append(filename)

# Remove zip files that dont match
zip_files = [f for f in zip_files if is_a_song(f)]

# Extract the song files
for zf in zip_files:
    with ZipFile(zf, 'r') as zipObj:
        zipObj.extractall()
        print(f"Extracted song file {zf}")
