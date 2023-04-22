import binascii
import os
import requests
import time


def get(url):
    """
    Caches GET requests responses for 12 hours. Note that this returns the
    response.text directly, not the response object.
    """

    directory_name = "cache"
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)

    response_text = ''
    cache_file = f'cache/{binascii.crc32(str.encode(url))}.txt'
    if os.path.isfile(cache_file) and os.stat(cache_file).st_mtime > time.time() - (60 * 60 * 12):
        print(f"Using cache file {cache_file} for {url}")
        with open(cache_file) as f:
            response_text = f.read()
    else:
        print(f"Requesting data for {url}")
        with open(cache_file, 'w') as f:
            req = requests.get(url)
            response_text = req.text
            f.write(response_text)

    return response_text
