# Prueba con clases

class empleado:
    def __init__(self, identificador, nombre, edad):
        self.id     = identificador
        self.nombre = nombre
        self.edad   = edad
    
    def get_data(self):
        print('El empleado con ID = {} de nombre {} tiene {} años'.format(self.id, self.nombre, self.edad))


a = empleado(1, 'Juan', 25)

a.get_data()