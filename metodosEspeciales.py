class CD:

    def __init__(self,autor,titulo,canciones):
        self.autor= autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"album: {self.titulo} de {self.autor} con {self.canciones} canciones."

mi_cd = CD("e","o",3)
print(mi_cd)