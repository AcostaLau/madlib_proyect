import random

numeroRandom = []

intro = "Este juego se trata de adivinar el numero que se genera aleatoriamente cada vez que le das al play.Los numeros que se generaran seran del 1 al 100. Suerte!"


def generarRandom():
    n_random = random.randint(1, 100)
    numeroRandom.append(n_random)


contador = 0

# Funcion para iniciar a jugar


def jugar():
    # declaro la variable contador global para poder usarla dentro de la funcion
    global contador
    n_usuario = int(input('Adivina el numero: '))

    # genero un while para que el usuario no salga del bucle hasta que haya adivinado la palabra
    while n_usuario != numeroRandom[0]:
        contador += 1
        if n_usuario != numeroRandom[0]:
            print('Incorrecto, intenta de nuevo')
            # Primera pista
            if contador == 5:
                pista = numeroRandom[0] % 2
                print('Veo que se te esta complicando! Te voy a dar una pista!')
                if pista == 0:
                    print('El numero es par!')
                else:
                    print('El numero es impar')
            # segunda pista
            elif contador == 10:
                if n_usuario > numeroRandom[0]:
                    print(
                        'Segunda pista! El numero es menor al ultimo numero que has puesto')
                else:
                    print(
                        'Segunda pista! El numero es mayor al ultimo numero que has puesto')
            n_usuario = int(input('Adivina el numero: '))
    print('Excelente! numero correcto')
    repetir()


def repetir():
    numeroRandom.pop()
    pregunta = int(input(
        'Quieres volver a jugar? Si es asi coloca el 1 si no coloca 2 para cerrar el juego: '))
    if pregunta == 1:
        generarRandom()
        print(numeroRandom[0])
        jugar()
    else:
        print('Gracias, adios.')


def iniciarJuego():
    generarRandom()
    print(intro)
    print(numeroRandom[0])
    jugar()


iniciarJuego()
