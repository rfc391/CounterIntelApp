
# Immudb Integration
import immudb.client
import requests

# IPFS API Endpoint
IPFS_API_URL = "http://localhost:5001/api/v0"

# Immudb client setup
immu_client = immudb.client.ImmuClient()
immu_client.login(username="immudb", password="immudb")

# Write to Immudb
def write_to_immudb(key, value):
    response = immu_client.set(key, value)
    return response

# Read from Immudb
def read_from_immudb(key):
    response = immu_client.get(key)
    return response

# Write to IPFS
def write_to_ipfs(data):
    files = {"file": ("data.txt", data)}
    response = requests.post(f"{IPFS_API_URL}/add", files=files)
    return response.json()

# Read from IPFS
def read_from_ipfs(cid):
    response = requests.get(f"{IPFS_API_URL}/cat?arg={cid}")
    return response.text

# Example: Archiving Immudb data to IPFS
def archive_immudb_to_ipfs(key):
    value = read_from_immudb(key).value.decode()
    ipfs_response = write_to_ipfs(value)
    return ipfs_response["Hash"]
