from random import choice
from time import sleep
from os import name, system

def komp():
    pilihan = ['batu', 'kertas', 'gunting']
    return choice(pilihan)

def banding(player, komputer):
    if(player == komputer):
        return 'Seri'
    elif(player == 'kertas' and komputer == 'gunting'):
        return 'Komputer menang'
    elif(player == 'kertas' and komputer == 'batu'):
        return 'Selamat kamu menang'
    elif(player == 'batu' and komputer == 'kertas'):
        return 'Komputer menang'
    elif(player == 'batu' and komputer == 'gunting'):
        return 'Selamat kamu menang'
    elif(player == 'gunting' and komputer == 'kertas'):
        return 'Selamat kamu menang'
    elif(player == 'gunting' and komputer == 'batu'):
        return 'Komputer menang'
        
def clear():
    if(name == 'nt'):
        system('cls')
    else:
        system('clear')

print('=========== GAME ===========')    
print('==== Batu Kertas Gunting ===')    
print('============================ \n') 
sleep(0.2)
while True:
    pemain = str(input('Pilih batu, ketas, atau gunting : ')).lower()
    komputer = komp()
    hasil = banding(pemain, komputer)
    if(not (pemain == 'batu' or pemain == 'kertas' or pemain == 'gunting')):
        print('INPUT SALAH!!!')
    else:
        print(pemain,'vs',komputer,'\n')
        print(hasil)
    sleep(2)
    print('\nMau main lagi ?')
    x = str(input('ya/tidak :'))
    if( x == 'tidak'):
        print('\nterima kasih sudah bermain')
        break
    else:
        clear()