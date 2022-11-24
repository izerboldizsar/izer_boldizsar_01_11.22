from data import *
from os import system

def menu():
    system('cls')
    print('0 - Kilépés')
    print('1 - Zenészek')
    print('2 - Albumok')
    print('3 - Értékelések')
    print('4 - Új album felvétele')
    print('5 - Új zenész felvétele')
    print('6 - Új értékelés felvétele')
    print('7 - Zenész törlése')
    print('8 - Album törlése')
    print('9 - Értékelés törlése')
    print('A - Mentés fájlba')
    return input('kérem válasszon: ')