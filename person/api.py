import httpx
from . import models
from .random_point import random_point


class Geois2Client:
    RESOURCE_ID = 8800
    BASE_URL = f'https://geois2.orb.ru/api/resource/8800'

    def __init__(self):
        self.client = httpx.Client(
            base_url=self.BASE_URL,
            headers={
                'Accept': 'application/json',
                'Authorization': 'Basic aGFja2F0aG9uXzI1OmhhY2thdGhvbl8yNV8yNQ=='
            }
        )

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
        resp = self.client.post('/feature/', json=data)
        resp_js = resp.json()
        return resp_js['id']

client = Geois2Client()

if __name__ == '__main__':
    client.create_person()

