import os
import requests
import json
from dotenv import load_dotenv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
}


def load_env():
    load_dotenv()
    env = os.environ
    return dict(env)


def login(url, email, password):
    data = {
        'email': email,
        'passwd': password
    }
    response = requests.post(url=url, data=data, headers=headers)
    if response.status_code != 200:
        return None
    try:
        data = json.loads(response.text)
        return data['token']
    except:
        print('登录失败')
        return None


def checkin(url, token):
    headers['Access-Token'] = token
    response = requests.get(url=url, headers=headers)
    try:
        data = json.loads(response.text)
        print(data['result'])
    except:
        print('签到失败')


def main():
    env = load_env()
    login_url = env['BASE_URL'] + '/api/token'
    checkin_url = env['BASE_URL'] + '/api/user/checkin'
    email = env['EMAIL']
    password = env['PASSWORD']
    token = login(url=login_url, email=email, password=password)
    if token is not None:
        checkin(url=checkin_url, token=token)


if __name__ == '__main__':
    main()
