import random

MIN_STRING_LENGTH = 15
MAX_STRING_LENGTH = 25
MIN_NUMBER = 1
MAX_NUMBER = 6

# Virknes ģeneratora klase, kas atbild par virknes ģenerēšanu spēles sākumā
class Generator():
    def generate_string():
        string_length = random.randint(MIN_STRING_LENGTH, MAX_STRING_LENGTH)
        string = ''.join([str(random.randint(MIN_NUMBER, MAX_NUMBER)) for number in range(string_length)])
        return string
