import os 
import pathlib
from pathlib import Path
import random

    
def musik_time_kek():
    dir_path = pathlib.Path.cwd()
    path = Path(dir_path, 'musik')
    dirname = str(path)
    ext = ('.mp3')
    musik_229 = []
    for files in os.listdir(dirname):
        if files.endswith(ext):
            musik_229.append(files)
        else:
            continue
    print(len(musik_229))
    musik_random = random.randint(1, len(musik_229))
    out = open('{0}\{1}'.format(dirname, musik_229[musik_random]))
    print(out)
    
musik_time_kek()
