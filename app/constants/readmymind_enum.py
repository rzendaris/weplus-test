from enum import Enum


class QuestionEnum(Enum):
    GREATER_THAN = u'Apakah angka nya lebih besar dari {0} ?'
    LESS_THAN = u'Apakah angka nya lebih kecil dari {0} ?'
    EQUAL = u'Apakah angka nya adalah {0} ?'