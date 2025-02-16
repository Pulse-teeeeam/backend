import httpx
from . import models
from .random_point import random_point
import requests


class Geois2Client:
    RESOURCE_ID = 8800
    BASE_URL = f'https://geois2.orb.ru/api/resource/8800'

    def __init__(self):
        self.client = requests.Session()
        self.client.headers = {'Accept': 'application/json',
                               'Authorization': 'Basic aGFja2F0aG9uXzI1OmhhY2thdGhvbl8yNV8yNQ=='
                               }


    def get(self):
        resp = self.client.get('')
        print(resp.text)
        print(resp.url)

    def create_person(self, person: models.Person.objects):
        data = {
            'extensions': {
                'attachment': None,
                'description': None,
            },
            'fields': {
                'num': person.id,
                'n_raion': person.place_of_birth,
                'fio': f'{person.first_name} {person.last_name} {person.middle_name}',
                'years': f'{person.burial_place} - {person.date_of_death}',
                'info': f'{person.biography}',
                'kontrakt': person.armed_conflict.title,
                'nagrads': f'{[medal.title for medal in person.medals.all()]}'
            },
            'geom': random_point(person.place_of_birth)
        }
        resp = self.client.post(self.BASE_URL + '/feature/', json=data)
        resp_js = resp.json()
        return resp_js['id']

    def delete_person(self, person_id: int):
        data = [{'id': person_id}]
        resp = self.client.delete(self.BASE_URL + f'/feature/', json=data)
        resp_js = resp.json()
        print(resp_js)


client = Geois2Client()

if __name__ == '__main__':
    client.delete_person(541)

