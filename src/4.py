
import random

def get_random_code(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    code = ''
    for _ in range(length):
        code += random.choice(characters)
    return code