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
    print('5 - Zenész törlése')
    print('6 - Album törlése')
    print('7 - Értékelés törlése')
    print('8 - Mentés fájlba')
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
        print(f'\t{i+1}. {artists[i]}')
    input()

def printAlbums():
    system('cls')
    print('Albumok listája:\n')
    for i in range(len(albums)):
        print(f'\t{i+1}. {albums[i]}')
    input()

def printRatings():
    system('cls')
    print('Értékelések listája:\n')
    for i in range(len(ratings)):
        print(f'\t{i+1}. {ratings[i]}')
    input()

def newAlbum():
    system('cls')
    print('--------Új albumok--------')
    bekertArtist=input('Zenész: ')
    bekertAlbum=input('Album: ')
    bekertRating=input('Értékelés: ')
    artists.append(str(len(artists))+'. '+bekertArtist)
    albums.append(str(len(albums))+'. '+bekertAlbum)
    ratings.append(str(len(ratings))+'. '+bekertRating)
    mentesFajlVegere(bekertArtist,bekertAlbum,bekertRating)
    input('Sikeres felvétel.')

def mentesFajlVegere(albums,artists,ratings):
    print(albums)
    file=open(filename,'a', encoding='utf-8')
    #file.write(f'\n{len(albums)+1}. {albums};{artists};{ratings}')
    file.write(f'\n{artists};{albums};{ratings}')
    file.close()
    input()