
import random
import time

elements = ('piedra','papel','tijera')
intentos = 0

while True:
    bot =random.choice(elements)
    you =input('elije (priedra/papel/tijera):  ')

    if  you not in (elements):
        print('elemento no valido, usa uno de los siguientes (piedra/papel/tijera): ')
        continue

    #se acumulan los intentos
    intentos += 1
    if you == 'piedra' and bot == 'piedra':
        print(f'empate  tu:({you})  -  bot:({bot})')
        time.sleep(1)
    elif you == 'papel' and bot == 'papel':
        print(f'empate  tu:({you})  -  bot:({bot})')
        time.sleep(1)
    elif you == 'tijera' and bot == 'tijera':
        print(f'empate  tu:({you})  -  bot:({bot})')
        time.sleep(1)
    elif you == 'piedra' and bot == 'papel':
        print(f'perdistes  tu:({you})  -  bot:({bot})')
        time.sleep(1)
    elif you == 'papel' and bot == 'tijera':
        print(f'perdistes  tu:({you})  -  bot:({bot})')
        time.sleep(1)
    elif you == 'tijera' and bot == 'piedra':
        print(f'perdistes  tu:({you})  -  bot:({bot})')
        time.sleep(1)
    elif you == 'piedra' and bot == 'tijera':
        print(f'ganastes  tu:({you})  -  bot:({bot})')
        time.sleep(1)
        break
    elif you == 'papel' and bot == 'piedra':
        print(f'ganastes  tu:({you})  -  bot:({bot})')
        time.sleep(1)
        break
    elif you == 'tijera' and bot == 'papel':
        print(f'perdistes  tu:({you})  -  bot:({bot})')
        time.sleep(1)
        break


print(f'el juego termino con intentos:({intentos})')