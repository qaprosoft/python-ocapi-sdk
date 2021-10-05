# Python module for OCAPI (under development)

## How to use

### Prequisites

- [OCAPI settings](https://github.com/SalesforceCommerceCloud/ocapi-settings) must be added to the instance under test.
- pip install requirements.txt
- [docs](https://documentation.b2c.commercecloud.salesforce.com/DOC1/topic/com.demandware.dochelp/OCAPI/current/shop/Resources/index.htm)

### Authentication with OCAPI can happen one of two ways

1. You can create a file named `.pycapi` at the root of the repo using the following format (Not tested on Windows).

```shell
[default]
client_id = <CLIENT_ID>
client_secret = <CLIENT_SECRET>
hostname = <INSTANCE_URI>
api_version = v20_4
```

2. Manualy supply credentials through an API instance.

```python
from ocapi.client import ShopAPI

api = ShopAPI(hostname='<INSTANCE_URI>', client_id='<CLIENT_ID>', client_secret='<CLIENT_SECRET>', api_version='
   ...: v20_4')

access_token = api.get_access_token()

api.product_search(
   site_id='en-US', 
   query='rings', 
   access_token=access_token, 
   start=0, 
   count=25, 
   refine_1='<refinement1>', 
   refine_2='<refinement2>', 
   refine_3='<refinement3>', 
   refine_4='<refinement4>', 
   refine_5='<refinement5>', 
   expand='prices, availability, images, variations, represented_products'
)
```

**Note: The above uses the shop apis product_search endpoint [docs](https://documentation.b2c.commercecloud.salesforce.com/DOC1/topic/com.demandware.dochelp/OCAPI/current/shop/Resources/ProductSearch.html). In order to fully utilize the search API, the product_search method will need to be improved, e.g. support data product_search endpoint to allow us to check for custom attributes on the given products.**

- Refinements represents attribute/value(s) pair
- Refinement attribute id and value(s) are separated by '='
- Multiple values are supported by a sub-set of refinement attributes and can be provided by separating them using a pipe (URL encoded = "|")
- Value ranges can be specified like this: refine=price=(100..500)
- Multiple refine parameters can be provided by adding an underscore in combination with an integer counter right behind the parameter name and a counter range 1..9:

```
refine_1=c_refinementColor=red|green|blue
```

The following system refinement attribute ids are supported:

```
   cgid: Allows to refine per single category id. Multiple category ids are not supported.
   price: Allows to refine per single price range. Multiple price ranges are not supported.
   pmid: Allows to refine per promotion id(s).
   htypes: Allow to refine by including only the provided hit types. Accepted types are 'product', 'master', 'set', 'bundle', 'slicing_group' (deprecated), 'variation_group'.
   orderable_only: Unavailable products will be excluded from the search results if true is set. Multiple
   refinement values are not supported.
```

### Output for product_search should be:

```shell
[{'_type': 'product_search_hit',
  'hit_type': 'master',
  'link': 'https://<INSTANCE>/s/en-US/dw/shop/v20_4/products/xxxxxxxx?q=rings&client_id=xxxxxxxxxxxxxxxxxx',
  'product_id': '188882C01',
  'product_name': 'Wrapped Open Infinity Ring',
  'product_type': {'_type': 'product_type', 'master': True},
  'represented_product': {'_type': 'product_ref',
   'id': '188882C01-48',
   'link': 'https://<INSTANCE>/s/en-US/dw/shop/v20_4/products/xxxxxxxxx-48?q=rings&client_id=xxxxxxxxxxxxxxxxxxxx'}},
...
```

### From here we can parse and compile a product URL from the product_id using SFCC controller Product-Search?pid={product_id}
