import os
import json
from pathlib import Path
import filetype


def rename(directory, name_format):
    directory = directory.rstrip('/')
    file_list = {}
    for file in os.listdir(directory):
        if file.startswith('.'):
            continue
        f = Path(f'{directory}/{file}')
        fs = f.stat()
        if f.is_file():
            fsize = fs.st_size
            if not file_list.get(fsize, None):
                file_list[fsize] = []
            file_list[fsize].append(f)
    idx = 0
    for key in sorted(file_list.keys())[::-1]:
        idx += 1
        for file in file_list[key]:
            kind = filetype.guess(str(file))
            name = f'{name_format % idx}.{kind.extension}'
            file.rename(file.parent.resolve() / name)
