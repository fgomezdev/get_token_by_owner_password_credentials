import requests

CLIENT_ID = 'my-client-id'
CLIENT_SECRET = 'my-client-secret'


def obtener_token(username, password):

    token_url = 'http://127.0.0.1/o/token/'

    token_data = {
        'grant_type': 'password',
        'username': username,
        'password': password,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }

    token_response = requests.post(token_url, data=token_data)

    if token_response.status_code == 200:
        return token_response.json()['access_token']

    raise Exception(f'Error al obtener el token:{token_response.json()}')


def consultar_api(token, api_url):
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()

    raise Exception(f'Error al realizar la consulta:{ response }')


if __name__ == '__main__':
    token = obtener_token('fernando', 'aeiou12345')
    result = consultar_api(token, 'http://127.0.0.1/api/v2/users')

    print(result)
