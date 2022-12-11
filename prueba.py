from datetime import date # Para obtener el año actual

# Definimos una clase Persona
class Persona:
    # Definimos los atributos de la clase
    nombre = ''
    apellidos = ''
    sexo = ''
    edad = 0
    ciudad = ''

    # Definimos un "constructor" para la clase que recibirá el nombre de la persona
    def __init__(self, nombre):
        self.nombre = nombre
    
    #Definimos los "setters"
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    
    def setSexo(self, sexo):
        self.sexo = sexo

    def setEdad(self, edad):
        self.edad = edad

    def setCiudad(self, ciudad):
        self.ciudad = ciudad

    #Definimos los "getters"
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos
    
    def getSexo(self):
        return self.sexo

    def getEdad(self):
        return self.edad

    def getCiudad(self):
        return self.ciudad

    def getApellidos(self):
        return self.apellidos
    
    # Ejemplo de método que devuelve el año de nacimiento en función de la edad
    def añoNacimiento (self):
        # Obtenemos la fecha actual
        fechaActual = date.today()
        # Obtenemos el año de la fecha actual
        año = fechaActual.year
        # Calculamos el año de nacimiento restando al año actual la edad de la persona
        añoNacimiento = año - self.edad
        return añoNacimiento

    #Definimos un método en la clase para mostrar todos los datos de la persona por pantalla
    def mostrarDatos(self):
        print('El nombre de la persona es: ' + self.nombre)
        print('La edad de la persona es: ' + str(self.edad))
        print('El sexo de la persona es: ' + self.sexo)
        print('La ciudad de la persona es: ' + self.ciudad)
    
    # Método para asignar el nombre completo a partir de los apellidos y el nombre    
    def generarNombreCompleto (self):
        global nombreCompleto
        nombreCompleto = self.apellidos + ', ' + self.nombre
        

#Fuera de la clase, definimos un objeto "ciudadano" de la clase Persona
#Le pasamos el nombre al constructor de la clase
ciudadano = Persona("Alonso Javier")

# Con los setters establecemos los datos del ciudadano
ciudadano.setApellidos('Lucas Sánchez')
ciudadano.setCiudad('Murcia')
ciudadano.setEdad(46)
ciudadano.setSexo('Hombre')

# Usamos el método de la clase que muestra los datos de la persona por pantalla
ciudadano.mostrarDatos()

# Usamos los setters y algún método de la clase para mostrar 
# algunos datos del objeto ciudadano de la clase Persona
print('El ciudadano ' + ciudadano.getNombre() + ' vive en ' + ciudadano.getCiudad() +
    ', nació en el año ' + str(ciudadano.añoNacimiento()))

# Llamamos al método que obtiene el nombre completo en la clase
ciudadano.generarNombreCompleto();

# Ejemplo de uso de variable global declarada en la clase Persona
# Para mostrar que no es necesario usar el nombre del objeto para usarla
print('El nombre completo es: ' + nombreCompleto)

# Declaramos un segundo objeto de la clase Persona
# para mostrar cómo trabajar con varios objetos de la misma clase
informatico = Persona("Vicenta Tomasa")
informatico.setApellidos('Buendía Fuenlabrada')
informatico.setCiudad('Madrid')
informatico.setEdad(34)
informatico.setSexo('Mujer')

#Datos del objeto informático
print('Datos del informático:')
informatico.mostrarDatos()
#Datos del objeto ciudadano
print('Datos del ciudadano:')
ciudadano.mostrarDatos()

# Si llamamos al método generarNombreCompleto y mostramos
# al ser variable global, tomará el valor de la última vez que fue llamada
# Aquí seguirá mostrando los datos del objeto "ciudadano"
print('El nombre completo del informático es: ' + nombreCompleto)

# Ahora mostrará los datos del "informático"
informatico.generarNombreCompleto()
print('El nombre completo del informático es: ' + nombreCompleto)

# Y ahora del ciudadano
ciudadano.generarNombreCompleto()
print('El nombre completo del ciudadano es: ' + nombreCompleto)