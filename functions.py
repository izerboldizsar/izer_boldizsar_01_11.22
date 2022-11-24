from data import *
from os import system

filename='data.csv'

def menu():
    system('cls')
    print('--------MENÜ--------')
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

def fajlbetoltes():
    file=open(filename,'r',encoding='utf-8')
    for row in file:
        darabolt=row.strip().split(';')
        artists.append(darabolt[0])
        albums.append(darabolt[1])
        ratings.append(float(darabolt[2]))
    file.close()

def printArtists():
    system('cls')
    print('Zenészek listája:\n')
    for i in range(len(artists)):
        print(f'\t{artists[i]}')
    input()