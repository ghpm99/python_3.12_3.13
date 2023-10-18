from typing import override


class Animal:
    def comunicar(self):
        return 'Não sei meu metodo de comunicação'


class Cachorro(Animal):

    @override
    def comunicar(self):
        return 'Au Au Au'


class Gato(Animal):

    @override
    def comunicar(self):
        return 'Miau'


class Pato(Animal):
    @override
    def comunicar(self):
        return 'Quack'

    @override
    def mover(self):
        return [1, 2, 3]


generic = Animal()
print(generic.comunicar())

cachorro = Cachorro()
print(cachorro.comunicar())

gato = Gato()
print(gato.comunicar())

pato = Pato()
print(pato.comunicar())
