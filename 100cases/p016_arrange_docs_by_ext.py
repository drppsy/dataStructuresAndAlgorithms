import os
import shutil


docs_dir = './docs'


def arrange_docs():
    for file in os.listdir(docs_dir):
        ext = os.path.splitext(file)[1]
        ext = ext[1:]
        if not os.path.isdir(f"{docs_dir}/{ext}"):
            os.mkdir(f"{docs_dir}/{ext}")
        source_path = f"{docs_dir}/{file}"
        target_path = f"{docs_dir}/{ext}/{file}"
        shutil.move(source_path, target_path)


arrange_docs()
