import requests
import json
from construct_url import construct_url
from construct_url import sku
from construct_url import encode
import sys




#armo un array de URL con su sku encodeado y lo guardo como array

api_key= sys.argv[1]

url = construct_url("https://api.woowup.com/apiv3/products/", api_key)

i=0
#Recorro el array de endpoints
for url_sku in (url):
    #Preparo el body con su sku correspondiente y le seteo demás parámetros
    prepare_payload = '{"sku":' +"\"{sku}\"".format(sku=sku[i]) + ','+ ' "name":' + "\" \"" + "," +  '"stock":0}'
    payload = prepare_payload
    # coloco headers
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        #Completar APIKEY del cliente
        'Authorization': 'Basic ' + api_key
    }
    #Hago el request
    response = requests.request("PUT", url_sku, headers=headers, data=payload)
    print(response.text)
    print('El sku ', sku[i], ' se ha actualizado correctamente, su sku encode es: ', encode(sku[i]))
    i += 1
#muestro la cantidad de productos actualizados
print('La cantidad de productos actualziados son: ', i)
