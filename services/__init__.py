from settings import settings


class Service:

    def get_header(self) -> dict:
        return {
            'authorization': 'Bearer {}'.format(settings.API_KEY)
        }