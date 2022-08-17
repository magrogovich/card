import json
import time
test = True
while test == True:

    response_API = requests.get('http://196.235.234.193:7779/')
    data = response_API.text
    back = json.loads(data)

    id =back['id']
    lat =back['lat']
    lng =back['lng']
    speed =back['speed']
    sat =back['sat']

    print(f"id:{id} lat:{lat} lng:{lng} speed:{speed} sat:{sat}\n")
    time.sleep(0.5)

