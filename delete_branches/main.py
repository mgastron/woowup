import requests
import json
import sys
from getBranches import get_branches



#armo un array de URL con su sku encodeado y lo guardo como array

api_key= sys.argv[1]
mail = sys.argv[2]
url = "https://api.woowup.com/apiv3/branches"

ids = get_branches(api_key)
i = len(ids)


#Recorro el array de endpoints
for id in ids:
    #Preparo el body con su sku correspondiente y le seteo demás parámetros
    prepare_payload = '{"id":' + id + ','+ ' "notify_to":' +  "\"{mail}\"".format(mail=mail) + '}'
    payload = prepare_payload
    # coloco headers
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        #Completar APIKEY del cliente
        'Authorization': 'Basic ' + api_key
    }
    
    print(prepare_payload)
    #Hago el request
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(response.text)
    print('El branch con id ', id, ' ha sido eliminado correctamente')
#muestro la cantidad de productos actualizados
print('La cantidad de tiendas eliminadas son: ', i)
