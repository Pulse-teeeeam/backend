import urllib

from pulse_backend import settings
import urllib.parse
import httpx

class ELCClient:
    BASE_URL = 'https://lk.orb.ru/api'

    def __init__(self, client_id, client_secret):
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
            'client_secret': getattr(settings, 'ELC_SECRET', ''),
            'redirect_url': getattr(settings, 'ELC_REDIRECT', ''),
            'grant_type': 'authorization_code',
        }

    def _get_info(self, access_token):
        self.



client = ELCClient()

if __name__ == '__main__':
    print(client.generate_url())
