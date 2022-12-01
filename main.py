from functions import*
from os import system

fajlbetoltes()

choice=''
while choice!='0':
    choice=menu()
    if choice=='1':
        printArtists()
    elif choice=='2':
        printAlbums()
    elif choice=='3':
        printRatings()
    elif choice=='4':
        newAlbum()
    elif choice=='5':
        pass
    elif choice=='6':
        pass
    elif choice=='7':
        pass
    elif choice=='8':
        pass