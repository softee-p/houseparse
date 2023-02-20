from tools import start_cont, offload, process, sleep
import requests


url = "https://www.spitogatos.gr/n_api/v1/properties/search-results"
filename = "attiki.json"
#temp results until first request
results = 10000

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"
cookie1 = ""
cookie2 = ""
querystring = {"listingType":"sale","category":"residential","sortBy":"price","sortOrder":"asc","latitudeLow":"37.836361","latitudeHigh":"38.151297","longitudeLow":"23.485336","longitudeHigh":"23.957062","zoom":"11","offset":"0"}
# headers = { "cookie": f'{cookie1}',
headers = {
        "User-Agent": f'{ua}',
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "el",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://www.spitogatos.gr/pwliseis-katoikies/anazitisi-xarti?latitudeLow=37.819006&latitudeHigh=38.121323&longitudeLow=23.517609&longitudeHigh=24.081688&zoom=12",
        "Cookie": f'{cookie2}',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        "TE": "trailers"
    }

loot = start_cont(filename)
querystring['offset'] = len(loot)
while querystring['offset'] < results - 30:
    print("gathering ", querystring['offset'], "-", querystring['offset'] + 30, " of ", results)
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    temp = process(response, loot)
    if not temp:
        break
    else:
        results = temp[0]
        loot = temp[1]
    querystring['offset'] = len(loot)
    sleep(15,30)

offload(filename, loot)
