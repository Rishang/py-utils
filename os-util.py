import requests
import os
import logging
import platform
import shutil
import sys
from utils import sh

try:
    from magic.compat import detect_from_filename
except ImportError:
    print(
        "[red]Failed to find libmagic.  Check your installation\n"
        "refer this url to install libmagic first: https://github.com/ahupp/python-magic#installation [/]"
    )
    sys.exit(1)


def download(requests_session, url: str, at: str):
    """Download a file"""

    file = requests_session.get(url, stream=True)
    if not os.path.exists(at):
        os.makedirs(at)

    file_name: str = url.split("/")[-1]
    if file.status_code == 200:
        with open(f"{at}/{file_name}", "wb") as fw:
            fw.write(file.content)
        logging.info(f"""Downloaded: \'{file_name}\' at {at}""")
        return f"{at}/{file_name}"
    else:
        logging.info(f"url: {url}, status_code: {file.status_code}")
        exit()


def extract(path: str, at: str):
    """Extract tar file"""

    try:
        system = platform.system().lower()
        file_info = detect_from_filename(path)

        if file_info.mime_type == "application/x-7z-compressed":
            if system in ["linux"]:
                cmd = f"7z x {path} -o{at}"
                logging.debug("command: " + cmd)
                sh(cmd)
            elif system == "windows":
                # 'C:\Program Files\\7-zip\\7z.exe'
                ...
        else:
            shutil.unpack_archive(path, at)

        return True
    except:
        logging.error(f"can't extract: {path}")
        raise Exception("Invalid file")
