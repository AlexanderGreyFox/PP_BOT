import aiohttp
import os
import urllib.parse

base_url = os.environ.get('URL')


class BaseAPI:
    def __init__(self):
        self.session = aiohttp.ClientSession(base_url=base_url)

    async def _close_(self):
        await self.session.close()

    async def get(self, path, headers=None, query=None):
        url = urllib.parse.urljoin(base_url, path)

        await self.session.get(url, headers=headers, params=query)
        await self._close_()

    async def post(self, path, headers=None, data=None):
        url = urllib.parse.urljoin(base_url, path)

        await self.session.post(url, headers=headers, data=data)
        await self._close_()


class NutritionAPI(BaseAPI):
    async def recipe_details(self, data):
        path = '/api/nutrition-details'
        resp = await self.post(path, data=data)
        return resp
