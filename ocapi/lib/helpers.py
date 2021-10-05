import random

import requests


def get_product(hostname, site_id, links):
    resp = requests.get(random.choice(links)).json()
    product_link = 'https://{0}/{1}/{2}/{3}/{4}/{5}.html'.format(
        hostname,
        site_id,
        resp['c_primaryCategory'],
        resp['primary_category_id'],
        resp['name'].replace(' ', '-').lower(),
        resp['id'])
    return product_link