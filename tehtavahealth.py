
import requests

url = "http://13.95.70.19/health.html"
r = requests.get(url)
if r.status_code == 200 :
    print(r)
else :
    print("okoko")
        

