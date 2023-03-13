import webbrowser

import requests

pageurl = 'https://www.onet.pl'

lista_dat = {20040629, 20120629, 20220913}


for data in (lista_dat):
    url = 'https://archive.org/wayback/available?url=' + pageurl + '&timestamp=' + str(data)
    response = requests.get(url)
    temp = response.json()
    page = temp["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)
    continue


