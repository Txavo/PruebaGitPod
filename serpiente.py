import pygame

# Define algunas constantes para representar los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Inicializa Pygame
pygame.init()

# Establece el tamaño de la pantalla
PANTALLA_ANCHO = 800
PANTALLA_ALTO = 600
pantalla = pygame.display.set_mode([PANTALLA_ANCHO, PANTALLA_ALTO])

# Establece el título de la ventana
pygame.display.set_caption('Serpiente')

# Se utilizará un reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Esta es la serpiente. Inicialmente consiste en un solo cuadro.
serpiente = [(200, 200)]

# La serpiente comienza moviéndose hacia la derecha
direccion = 'DERECHA'

# Esta es la manzana. Inicialmente se ubica en una posición aleatoria.
manzana = (300, 300)

# Controla si el juego está en curso o ha terminado
juego_en_curso = True

# Bucle principal del juego
while juego_en_curso:
    # Procesa cualquier evento de teclado que se haya producido
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            # Cambia la dirección de la serpiente de acuerdo a la tecla presionada
            if evento.key == pygame.K_LEFT:
                direccion = 'IZQUIERDA'
            elif evento.key == pygame.K_RIGHT:
                direccion = 'DERECHA'
            elif evento.key == pygame.K_UP:
                direccion = 'ARRIBA'
            elif evento.key == pygame.K_DOWN:
                direccion = 'ABAJO'

# Actualiza la posición de la serpiente de acuerdo a la dirección en la que se encuentre
if direccion == 'IZQUIERDA':
    nueva_cabeza = (serpiente[0][0] - 10, serpiente[0][1])
elif direccion == 'DERECHA':
    nueva_cabeza = (serpiente[0][0] + 10, serpiente[0][1])
elif direccion == 'ARRIBA':
    nueva_cabeza = (serpiente[0][0], serpiente[0][1] - 10)
elif direccion == 'ABAJO':
    nueva_cabeza = (serpiente[0][0], serpiente[0][1] + 10)

# Verifica si la serpiente ha chocado contra un borde o contra su propio cuerpo
if nueva_cabeza[0] < 0 or nueva_cabeza[0] >= PANTALLA_ANCHO or nueva_cabeza[1] < 0 or nueva_cabeza[1] >= PANTALLA_ALTO or nueva_cabeza in serpiente:
    juego_en_curso = False
else:
    # Si la serpiente no ha chocado, agrega la nueva cabeza a la serpiente y elimina la última parte del cuerpo
    serpiente.insert(0, nueva_cabeza)
    if serpiente[0] == manzana:
        # Si la serpiente come una manzana, genera una nueva manzana en una posición aleatoria
        manzana = (random.randint(0, PANTALLA_ANCHO // 10 - 1) * 10, random.randint(0, PANTALLA_ALTO // 10 - 1) * 10)
    else:
        serpiente.pop()

# Dibuja la pantalla
pantalla.fill(NEGRO)
for posicion in serpiente:
    pygame.draw.rect(pantalla, BLANCO, pygame.Rect(posicion[0], posicion[1], 10, 10))
pygame.draw.rect(pantalla, VERDE, pygame.Rect(manzana[0], manzana[1], 10, 10))

# Actualiza la pantalla
pygame.display.flip()

# Controla la velocidad del juego
reloj.tick(10)

# Finaliza Pygame
pygame.quit()
