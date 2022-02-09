import random
from config import Config


class CustomUtils:

    def __init__(self):
        pass

    @staticmethod
    def generate_random_number(number_collection):
        number = random.randint(0, int(Config.MAX_NUMBER))
        if len(number_collection) <= int(Config.MAX_NUMBER):
            if any(x['number'] == number for x in number_collection):
                number = CustomUtils.generate_random_number(number_collection)
        else:
            number = -1
        return number