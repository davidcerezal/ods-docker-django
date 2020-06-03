from odds.domain.models.betType import BetType


class BetTypeFactory(object):

    @classmethod
    def create(cls, identifier, description, value, name=''):
        name = identifier if name == '' else name
        return BetType(name=name, identifier=identifier, value=value)
