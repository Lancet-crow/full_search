import sys
from io import BytesIO

import requests
from PIL import Image

from geocoder import get_ll_span

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'

toponym_to_find = " ".join(sys.argv[1:])

ll, span = get_ll_span(toponym_to_find)
pt = ll + f",pm2rdl"

map_params = {
    "pt": pt,
    "ll": ll,
    "spn": span,
    "l": "map"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
