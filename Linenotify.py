

import requests
def Linenotify(msg):

    url = 'https://notify-api.line.me/api/notify'
    token = "kWqvDAx6OXTFstbfjPBl2rQXYA6KkMPlk2QBUjpglsP"
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}


    requests.post(url, headers=headers , data = {'message':msg})

