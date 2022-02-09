import random
from config import Config


class CustomUtils:

    def __init__(self):
        self.max_number = int(Config.MAX_NUMBER)
        self.min_number = 0
        super(CustomUtils, self).__init__()

    def generate_random_number(self, list_number):
        number = -1
        if len(list_number) > 0:
            index = int(len(list_number) / 2)
            number = list_number[index]['number']
        return number