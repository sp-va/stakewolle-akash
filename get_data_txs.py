import requests
import pybase64

def get_data(block_height: str):

    api_url = f'https://akash-rpc.w3coins.io/block?height={block_height}'

    response = requests.get(api_url)

    data_transactions = response.json().get("result").get('block').get('data').get('txs')

    decoded_list = []

    for transaction in data_transactions:
        dec = pybase64.b64decode(transaction)
        decoded_list += dec
        print('\n', dec, type(dec), '\n')
    return decoded_list

    

print(get_data('11260637'))



