# Help you to make the POST, GET, PATCH, PUT and DELETE

import json
import requests


def get_request(url, auth):
    response = requests.get(url=url, auth=auth)
    return response.json()
