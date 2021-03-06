import os
import shutil

import requests


def get_data_from_binary(url):
    response = requests.get(url, stream=True)
    return response.raw


def save_image(folder, name, data):
    filename = os.path.join(folder, name + '.jpg')
    with open(filename, 'wb') as fout:
        shutil.copyfileobj(data, fout)


def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_binary(url)
    save_image(folder, name, data)