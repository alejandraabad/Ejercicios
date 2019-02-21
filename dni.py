class NIF():
    def __init__(self, numero):
        self.numero = numero

    def calcular_letra(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        valor = int(self.numero/23)
        resto = self.numero-23*valor
        letra = letras[resto]
        return letra

c = NIF(2338772)
print(c.calcular_letra())
