import base64
from get_products import get_products
import sys

#defino los sku a actualizar
sku = get_products(sys.argv[1])

#Encodeo los sku
def encode(sku):
    sku_encode = sku.encode('ascii')
    base64_bytes = base64.b64encode(sku_encode)
    base64_sku = base64_bytes.decode('ascii')
    return base64_sku
#devuelvo el sku en base 64


#Construyo la URL con el producto en base 64
def construct_url(url, api_key):
    url_encode = []
    for into_base64 in sku:
        sku_encode = encode(into_base64)
        url_encode.append(url + sku_encode)
    return url_encode
#devuelvo un array de todas las URL




