import requests
import base64
from time import sleep


class VkAPI:

    def search_victims(self, age_from, age_to, victim, group_id=0):

        params = {
            'q': '',
            'fields': 'sex,bdate,city,country,books,music,interests',
            'age_from': age_from,
            'age_to': age_to,
            'sex': victim.sex_search,
            'city': victim.city,
            'country': victim.country,
            'has_photo': 1,
            'group_id': group_id,
            'count': 1000,
            'v': self.version,
            'access_token': self.access_token
        }
        data = self.__request('/users.search', params)
        return data['response']['items']

    def __init__(self):

        self.url = 'https://api.vk.com/method'
        self.version = 5.101
        self.user = ''
        self.access_token = ''
        self.respond_success = True
        with open('token') as token:
            coded_token = token.readline()
            self.access_token = base64.b64decode(coded_token).decode('utf-8')
        params = {
            'v': self.version,
            'access_token': self.access_token
        }

        self.user_access = self.__request('/users.get', params)

    def __request(self, method, params):

        result_api = requests.get(f'{self.url}{method}', params=params)

        data = 'Error'

        if result_api.status_code == 200:
            data = result_api.json()
        else:
            print('Что-то пошло не так ...', result_api)

        return data


    def user_info(self, user_id):

        params = {
            'user_ids': user_id,
            'fields': 'photo_200,sex,city,country,books,music,interests',
            'v': self.version,
            'access_token': self.access_token
        }

        data = self.__request('/users.get', params)
        try:
            data = data['response'][0]
            self.user = data['id']
        except KeyError:
            data = {}
        return data

    def groups(self, user_id):

        params = {
            'user_id': user_id,
            'v': self.version,
            'access_token': self.access_token
        }

        while self.respond_success:

            data = self.__request('/groups.get', params)
            try:
                groups_get = data['response']['items']
                self.respond_success = False
            except KeyError:
                if data['error']['error_code'] == 6:
                    sleep(0.5)
                else:
                    groups_get = []
                    self.respond_success = False

        self.respond_success = True

        return groups_get

    def photo(self, victim_id):

        params = {
            'owner_id': victim_id,
            'extended': 1,
            'album_id': 'wall',
            'count': 100,
            'v': self.version,
            'access_token': self.access_token
        }
        while self.respond_success:
            data = self.__request('/photos.get', params)
            try:
                data['response']['items']
                self.respond_success = False
            except KeyError:
                if data['error']['error_code'] == 6:
                    sleep(0.5)
                else:
                    data = []
                    self.respond_success = False

        self.respond_success = True
        return data


