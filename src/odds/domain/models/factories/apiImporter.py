from odds.domain.models.apiImporter import ApiImporter


class ApiImporterFactory(object):

    @classmethod
    def create(cls, api, key, date, limit):
        return ApiImporter(api=api, key=key, date=date, limit=limit, counter=0)
