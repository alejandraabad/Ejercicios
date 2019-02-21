class Contador():
    def __init__(self, contador):
        self.contador = contador

    def aumenta_contador(self):
        return self.contador + 1
    def disminuye_contador(self):
        return self.contador - 1
c = Contador(5)
print(c.aumenta_contador())
