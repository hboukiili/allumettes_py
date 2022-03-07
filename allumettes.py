import os
from random import randrange
from math import ceil
#ce fichier affiche le code du jeu d'alumettes
def allumettes():
    x = randrange(15,30)  #nombre d'allumettres aleatoire
    print("le nombre d'allumettes est ", x)
    y = input("souhaitez vous jouer en premiez ?\noui ou non ? ") #le joueur decide s'il veut etre le prmier a jouer ou non
    while y != 'non' and y != 'oui':
        y = input ("veuillez repondre par oui ou non : ")    
    if y == 'non':  #une condition si le joueur a decider a ne pas commecer.
        r = x % 4
        if r == 0:
            r = randrange(1,3)
            print("j'en prends :", r)
            x = x - r 
        else:
            print("j'en prends :", r)
            x = x - r
        print ("il en reste :", x)
    while x > 0 :
        n = int (input ("veuillez entrer le nombre : ")) #on demande au joueur le nombre d'allumemt qu'il souhaite prendre
        while n < 1 or n > 3 or n > x :
            n = int(input("veuillez entrer un nombre entre 1 et 3 : "))
        x = x - n
        if x <= 0: #une condition si le nombre est : 0. Dnc l'ordinateur a perdu. 
            print ("il en reste : ", x) 
            print ("j ai perdu!") 
        else:
            print("il en reste ", x) #condition pour printer le reste des allimentes
            l = x % 4   #checker si les allimentes sont des multiples de 4
            if l == 0:  
                l = randrange(1,3)  #condition pour choisir aleatoirement si le reste n'est pas de multiples de 4
            print("j'en prends ", l)
            x = x - l
            print ("il en reste", x)
            if x <= 0:
                print ("vous avez perdu")
    a = input("vous voullez jouez encore ? \n oui ou non " )
    while (a != 'oui' and a != 'non'):
        a = input("veuillez repondre par oui ou non :") #voir si le joueur veut jouer encore une fois
    if (a == 'non'):
        print ("Merci pour votre visite, au revoir")
    else:
        allumettes()
print("pour demarrer le programme, veuilez tappez : allumettes()")
os.system("pause")
