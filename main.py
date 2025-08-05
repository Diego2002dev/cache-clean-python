import os
import tempfile
from cleaner import delete

if(__name__ == "__main__"):

    temp_url = tempfile.gettempdir()
    url_file = os.listdir(temp_url)

    if "Temp" not in str(temp_url):
        raise RuntimeError("[ERROR]")

    for file in url_file:   
        complete_url_file = os.path.join(temp_url, file)
        delete(file, complete_url_file)
