
import requests

DATABASE_ID = 'a5a53e0b-af35-4f87-89ac-7069f635e54b'
CLOUDFLARE_API_KEY = 'SqnVMNvjSXpDN9YCR_vf-cqlnsKjZAcJ4SrfEi5u'

def query_influxdb(query):
    url = f'https://api.cloudflare.com/client/v4/d1/databases/{DATABASE_ID}/query'
    headers = {
        'Authorization': f'Bearer {CLOUDFLARE_API_KEY}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json={"sql": query}, headers=headers)
    return response.json()

if __name__ == "__main__":
    result = query_influxdb("SELECT * FROM measurements")
    print(result)
