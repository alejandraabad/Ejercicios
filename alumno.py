class Alumno():
    def __init__(self,nombre,  numero_matricula, nota1, nota2, nota3):
        self.nombre = nombre
        self.numero_matricula = numero_matricula
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = nota1 + nota2 + nota3

    def nota_final(self):
        
        if (self.media / 3) >= 4.8:
            return self.nombre, self.numero_matricula, "Alumno aprobado"
        else:
            return self.nombre, self.numero_matricula,"Alumno suspenso"
Paco = Alumno("Paco", 26700, 5, 7, 8)
print(Paco.nota_final())
