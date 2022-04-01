import requests
import json
import time

# Traigo todos los productos de WoowUp con STOCK 0

# Inicializo la pagina y limite

def get_products(api_key):
    page = 0
    limit = 100

    i = 0
    list_sku = []
    # Recorro Request de todos los productos con stock
    while i == 0:

        url = "https://api.woowup.com/apiv3/products?page=" + str(page) + '&limit=' + str(limit) + "&with_stock=1"
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
                sku = str(response['payload'][n]['sku'])
                list_sku.append(sku) #Agrego los sku a una lista
            print('Estamos en la página: ', page)
            page += 1 # cambio de página
        except: #finalizo el procesamiento cuando obtenemos no obtengo más resultados.
            print('finalizó get de productos')
            i = 0
            break
        # print(response)
    print(list_sku)
    return list_sku

