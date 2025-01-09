
import immudb
from immudb.client import ImmudbClient

def connect_to_immudb():
    client = ImmudbClient()
    client.connect('2bf985f6bc3412ca90de78c00002ecaf.r2.cloudflarestorage.com', 3322)
    client.login('admin', 'SqnVMNvjSXpDN9YCR_vf-cqlnsKjZAcJ4SrfEi5u')
    return client

def store_data(client, key, value):
    client.set(key, value)

def retrieve_data(client, key):
    return client.get(key)

if __name__ == "__main__":
    client = connect_to_immudb()
    store_data(client, 'test_key', 'test_value')
    print(retrieve_data(client, 'test_key'))
