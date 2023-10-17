# PEP 709

a = 1
name = 'teste'

print([locals() for x in [1]])

animals = {
    'boi': 'muuuu',
    'cachorro': 'au au',
    'gato': 'miau'
}

print([f'O {animal} faz {sound}!' for animal, sound in animals.items()])
