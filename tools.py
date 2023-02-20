from time import sleep as slp
from os.path import exists
from random import randint
from os import remove
import json


def start_cont(filename):
    
    if exists(f'{filename}'):
        with open(filename, 'r', encoding='utf-8') as f:
            loot = json.load(f)
        print('Resuming from ', len(loot))
    else:
        loot = []
        print('STATUS: starting...')
    return loot


def process(response, loot):
    try:
        data = response.json()
        results = data['pagination']['totalResults']
        for house in data['data']:
            loot.append(house)
    except:
        print("got caught")
        return False
    return results, loot


def sleep(min, max):
    sleeptime = randint(min, max)
    print("STATUS: sleeping for: ", sleeptime, "seconds")
    slp(sleeptime)
    print("STATUS: resuming...")


def offload(filename, loot):
    print("STATUS: done gathering")
    print("STATUS: writing to file...")
    if exists(f'{filename}'):
        print("overwriting existing file ", filename)
        remove(f'{filename}')
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(loot, f, ensure_ascii=False, indent=4)
    print("STATUS: write complete")