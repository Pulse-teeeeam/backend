import urllib

from pulse_backend import settings
import urllib.parse
import httpx

class ELCClient:
    BASE_URL = 'https://lk.orb.ru/api'

    def __init__(self):
        self.client = httpx.Client(base_url=self.BASE_URL)

    def generate_url(self):
        data = {
            'client_id': getattr(settings, 'ELC_ID', ''),
            'redirect_uri': getattr(settings, 'ELC_REDIRECT', ''),
            'response_type': 'code',
            'scope': 'rsaag_id',
            'state': getattr(settings, 'ELC_STATE', ''),
        }

        return 'https://lk.orb.ru/oauth/authorize?' + urllib.parse.urlencode(data)

    def _get_token(self, code: str):
        data = {
            'client_id': getattr(settings, 'ELC_ID', ''),
            'client_secret': getattr(settings, 'ELC_TOKEN', ''),
            'redirect_uri': getattr(settings, 'ELC_REDIRECT', ''),
            'code': code,
            'grant_type': 'authorization_code',
        }

        resp = self.client.post('https://lk.orb.ru/oauth/token', json=data)
        resp_js = resp.json()
        return resp_js['access_token']

    def _get_info(self, access_token: str):
        data = {
            'scope': 'rsaag_id',
        }

        headers = {
            'Authorization': 'Bearer ' + access_token,
        }

        resp = self.client.get('https://lk.orb.ru/api/get_user', headers=headers, params=data)
        resp_js = resp.json()
        return resp_js['user']

    def auth(self, code: str):
        access_token = self._get_token(code)
        info = self._get_info(access_token)
        return info['id']

client = ELCClient()

if __name__ == '__main__':
    print(client.generate_url())
    print(client.auth(input('Enter code: ')))
