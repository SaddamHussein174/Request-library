from pprint import pprint
import requests
import os


# _____________________________Задача 1__________________________________________________________________________________


name_url = "https://superheroapi.com/api/2619421814940190/search/"
superheroes = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]

for hero in superheroes:
    hero_r = requests.get(name_url + hero['name'])
    hero['intelligence'] = int(hero_r.json()['results'][0]['powerstats']['intelligence'])

print(sorted(superheroes, key=lambda hero: hero['intelligence'])[0]['name'])


# ___________________________Задача 2___________________________________________________________________________________

TOKEN = 'AQA......AxkY'


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):

        """Метод загружает файлы по списку file_list на яндекс диск"""

        file_path = os.path.normpath(file_path)
        headers = {"Authorization": f'OAuth {self.token}'}
        files = {"file": open(file_path, 'rb')}
        response_url = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
        params = {"path": file_path},
        headers = headers)
        url = response_url.json().get('href')

        response_upload = requests.put(url, files=files, headers={})
        return print(response_upload.status_code)


if __name__ == '__main__':

# Получить путь к загружаемому файлу и токен от пользователя

    path_to_file = "C://Users/Александр/PycharmProjects/pythonProject3/тест.txt"
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
