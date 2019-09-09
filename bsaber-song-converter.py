import os
import re
import shutil
import subprocess

def main():
    # Add all folders to a list
    folders = []
    for root, dirs, files in os.walk('.'):
        for directory in dirs:
            folders.append(directory)

    # Split file paths into uneeded top level folders and core song folders
    core_folders = [f for f in folders if not re.match("^[0-9]+-[0-9]+", f)]
    toplevel_folders = [f for f in folders if re.match("^[0-9]+-[0-9]+", f)]

    # Put folder with song contents in base directory
    dest = './'

    # Remove top level folder
    for folder in toplevel_folders:
        for root, dirs, files in os.walk(f'./{folder}'):
            for directory in dirs:
                shutil.move(f'./{folder}/{directory}', dest)
        shutil.rmtree(f'./{folder}')

    # Convert the songs
    for folder in core_folders:
        subprocess.run(['songe-converter.exe', f'{folder}'])

if __name__ == '__main__':
    main()

