from typing import Protocol, runtime_checkable


# abstração do tipo ecommerce
@runtime_checkable
class Ecommerce(Protocol):
    slug: str
    url: str


# classe de seguros
class Seguros:
    purchases = 498


# seguros
seguros = Seguros()

# False
print(isinstance(seguros, Ecommerce))

# seguros agora se torna uma subclasse estrutural(structural typing)
# por implementar toda a estrutura de ecommerce e ecommerce ser uma declaração de protocolo
seguros.slug = 'seguros'
seguros.url = 'https://www.segurospromo.com.br/'

# True
print(isinstance(seguros, Ecommerce))

# nao é possivel alterar o protocolo em runtime
Ecommerce.id = 1

# True
print(isinstance(seguros, Ecommerce))
