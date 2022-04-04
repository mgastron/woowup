import requests
import json
import time

# Traigo todas las de WoowUp

# Inicializo la pagina y limite

def get_branches(api_key):
    page = 0
    limit = 100

    i = 0
    list_id = []
    # Recorro Request de todos los productos con stock
    while i == 0:

        url = "https://api.woowup.com/apiv3/branches/?page=" + str(page) + '&limit=' + str(limit)
        payload = {}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + api_key
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        time.sleep(1)
        # obtengo respuesta y la guardo convertida en json
        response = response.json()
        n = 0

        try:
            for n in range(limit):     # Recorro la respuesta y me guardo el listado de sku
                id = str(response['payload'][n]['id'])
                list_id.append(id) #Agrego los sku a una lista
            print('Estamos en la página: ', page)
            page += 1 # cambio de página
        except: #finalizo el procesamiento cuando obtenemos no obtengo más resultados.
            print('finalizó get de tiendas')
            i = 0
            break
        # print(response)
    #print(list_id)
    return list_id

