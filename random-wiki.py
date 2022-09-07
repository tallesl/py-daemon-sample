#! /usr/bin/python3

from http.client import HTTPSConnection
from json import loads
from time import sleep
from urllib.parse import urljoin

def get(host, url):
    print(f'GET {url}')

    connection = HTTPSConnection(host)
    connection.request('GET', url)

    response = connection.getresponse()
    location_header = response.getheader('location')

    if location_header is None:
        return response
    else:
        location = urljoin(url, location_header)
        return get(host, location)

try:
    while True:
        response = get('en.wikipedia.org', '/api/rest_v1/page/random/summary')

        response_object = loads(response.read())
        extract = response_object['extract']

        print(extract)
        sleep(5)
except KeyboardInterrupt:
    pass
