import random

MIN_STRING_LENGTH = 15
MAX_STRING_LENGTH = 26
MIN_NUMBER = 1
MAX_NUMBER = 6

class Generator():
    def generate_string(string_length):
        if string_length not in range(MIN_STRING_LENGTH, MAX_STRING_LENGTH):
            return None
        string = [random.randint(MIN_NUMBER, MAX_NUMBER) for number in range(string_length)]
        return string
