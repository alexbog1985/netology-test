import requests


class YaDiskApi:
    def __init__(self):
        self.TOKEN = ''  # Поменять на свой
        self.URL = 'https://cloud-api.yandex.net/v1/disk'
        self.headers = {
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.TOKEN}',
        }

    def new_dir(self, path):
        params = {
            'path': path,
        }
        response = requests.put(f'{self.URL}/resources', params=params, headers=self.headers)
        return response

    def delete_dir(self, path):
        params = {
            'path': path,
        }
        response = requests.delete(f'{self.URL}/resources', params=params, headers=self.headers)
        return response

    def info_dir(self, path):
        params = {
            'path': path,
        }
        response = requests.get(f'{self.URL}/resources', params=params, headers=self.headers)
        return response
