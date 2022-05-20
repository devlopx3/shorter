from flask import request,Flask
import requests
import urllib.request

app = Flask(__name__)



@app.before_request
def getAnalyticsData():
    global userIP, userCountry, userCity
    api =requests.get("https://www.iplocate.io/api/lookup/").json()
    userCountry = api['country']
    userCity = api['city']
    userIP = api['ip']
    
        




@app.route('/')
def st():
    return f'{userIP} - {userCity} - {userCountry}'
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    app.run(host='0.0.0.0', port=5000)	
