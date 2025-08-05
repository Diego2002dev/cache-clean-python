import os
import shutil

def force_remove(func, path, exc_info):
    try:
        os.chmod(path, 0o777)
        func(path)
    except Exception as e:
        print(f"[ERROR] {e} in {path}")

def delete(file, complete_url_file):
    try:
        if(os.path.isfile(complete_url_file) or os.path.islink(complete_url_file)):
            os.remove(complete_url_file)
        elif(os.path.isdir(complete_url_file)):
            shutil.rmtree(complete_url_file, ignore_errors=False, onexc=force_remove)
    except Exception as e:
        print(f"[ERROR] {e} \nFile '{file}' couldn't be removed")
        print(complete_url_file)
