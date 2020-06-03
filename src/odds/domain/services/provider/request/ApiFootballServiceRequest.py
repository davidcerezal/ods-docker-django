from odds.domain.models.factories.apiImporter import ApiImporterFactory
from odds.domain.models.apiImporter import ApiImporter
from odds.domain.services.provider.request.ServiceRequest import ServiceRequest
from datetime import date
import urllib3
import json

class ApiFootballServiceRequest(ServiceRequest):

    url_base = "https://api-football-v1.p.rapidapi.com"
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': ""
    }
    keys = {
        "ea209b38damsh346eea7dbd4ad5fp1041d7jsn59c4a929bbf2",
        "ea209b38damsh346eea7dbd4ad5fp1041d7jsn59c4a929bbf2"
    }

    next_fixtures = "/v2/fixtures/league/%league%/next/%number%?timezone=Europe/Madrid"
    odds = "/v2/odds/fixture/%fixture%"

    request_number = 20
    daily_limit = 95

    def __init__(self):
        ServiceRequest.__init__(self)
        self.http = urllib3.PoolManager()

    def __call(self, url):
        not_exceeded = False
        for key in self.keys:
            today_request = ApiImporter.objects.filter(date=date.today(), key=key)[0]
            if not today_request:
                today_request = ApiImporterFactory.create('ApiFootball', key, date.today(), self.daily_limit)
                today_request.save()

            if today_request.is_exeded():
                continue
            else:
                self.headers['x-rapidapi-key'] = key
                today_request.add_attemp()
                today_request.save()
                not_exceeded = True
                break

        if not_exceeded:
            print('Call::::%s', url)
            response = self.http.request('GET', url, headers=self.headers)
            return json.loads(response.data.decode('utf-8'))
        else:
            raise Exception("Api limit exceeded")

    def call_next_fixtures_by_league(self, league_item):
        response = self.__call(self.get_url_next_fixture(league_item))
        if response.get('api').get('results') <= 0:
            return False
        else:
            return response.get('api').get('fixtures')

    def call_get_odds_by_fixture(self, fixture_id):
        response = self.__call(self.get_url_odds_fixture(fixture_id))
        if response.get('api').get('results') <= 0:
            return False
        else:
            return response.get('api').get('odds')[0]

    def get_url_next_fixture(self, league_item):
        url = self.url_base + self.next_fixtures
        url = url.replace('%league%', str(league_item))
        url = url.replace('%number%', str(self.request_number))
        return url

    def get_url_odds_fixture(self, fixture):
        url = self.url_base + self.odds
        url = url.replace('%fixture%', str(fixture))
        return url




