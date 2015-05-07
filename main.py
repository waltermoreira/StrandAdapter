# file: main.py

import requests
import json

def list(arg):
    pass

def search(arg):

    # The requests object contains HTTP headers plus payload.
    # print r.headers
    # The remote service sets cookies. For now, we do not pass the cookie.
    # print headers['set-cookie']

    # The output may be ordered differently than the input.
    # In particular, the "sequence" tuple may be buried in the list.

    # Expect JSON argument like this python command.
    # Example:
    # main.search({'site': 'at_sRNA', 'list': 'strand'})
    # That equates to this URL.
    # 'http://mpss.udel.edu/web/php/pages/json.php?SITE=at_sRNA&list=strand&format=json'

    # The remote service takes additional parameters that we will pass from input args
    url = ('http://mpss.udel.edu/web/php/pages/json.php?SITE={site}&list={list}&format=json')

    rqst = requests.get(url)

    # If the response status is not 2xx, raise an exception with the
    # proper error message
    rqst.raise_for_status()

    # if we are here, it means the request was successful
    try:
        # try to decode the JSON response (it will succeed even if the
        # content type is not properly set, but the response is really
        # a JSON object)
        payload = rqst.json()
    except ValueError:
        raise Exception('could not decode JSON object')

    strand_data = payload['strand']
    for strand in strand_data:
        decoded = json.dumps(strand)
        print decoded
        print '---'
