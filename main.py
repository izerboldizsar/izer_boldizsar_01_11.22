from functions import*
from os import system



choice=''
while choice!='0':
    choice=menu()
    if choice=='1':
        fajlbetoltes()
        printArtists()
    elif choice=='2':
        fajlbetoltes()
        printAlbums()
    elif choice=='3':
        fajlbetoltes()
        printRatings()
    elif choice=='4':
        fajlbetoltes()
        newAlbum()
    elif choice=='5':
        fajlbetoltes()
        Torles()