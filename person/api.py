import httpx

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

    def create_person(self):
        resp = self.client.post('/feature/')
        print(resp.url)
        print(resp.text)


client = Geois2Client()

if __name__ == '__main__':
    client.create_person()

