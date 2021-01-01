# %%
from math import *
from random import *
from tkinter import *
import os
import time

# TODO Mettre en place les trois boutons échelles (utiliser get pour récupérer la valeur)
# TODO améliorer la déclaration des dimensions de notre fenêtre
# TODO créer une frame droite et une frame gauche pour séparer le menu et le jeu.
# FIXME c'est peut être dû à l'organisation avec une seule frame mais j'ai l'impression que mon tableau est coupé sur la droite et sur le bas...

fenetre = Tk()
fenetre.title("Le jeu de la vie")
frame_jeu_de_vie = Frame(fenetre, width=300, height=300)
frame_jeu_de_vie.pack()
canvas = Canvas(frame_jeu_de_vie, width=300, height=300)
canvas.pack()
#canvas = Canvas(fenetre, width=side*ligne, height=side*colonne)

M=[]
ligne= 50
colonne= 50



def initialiser():
    x = 10 # valeur fixée arbitrairement
    y = 10 # valeur fixée arbitrairement
    global ligne
    global colonne
    global rectangles
    rectangles = []
    for i in range(ligne):
        M.append([]) # Liste de liste qui contient les valeurs des cellules (1:vivante et 0:morte)
        rectangles.append([]) # Liste de liste qui contient tous les rectangles
        for j in range(colonne):
            rand = randint(0,1)
            rect = canvas.create_rectangle(x, y, x+10, y+10, fill="white") # (x,y) les coordonnées du coin supérieur gauche et (x+10, y+10) celles du coin inférieur droit.
            rectangles[i].append(rect)
            M[i].append(rand)
            x += 10 # l'ordonnée est fixé à 10, on incrémente "l'abscisse" uniquement (2ème boucle for)
        # on est dans la 1ere boucle for
        x = 10 # on fixe l'abscisse
        y += 10 # on incrémente l'ordonnée
           


def afficher_damier():
    os.system("clear")
    for i in range(ligne):
        for j in range(colonne):
            if M[i][j]==1:
                couleur = "red"
            else:
                couleur = "white" # mettre le end car /n par défaut
            canvas.itemconfig(rectangles[i][j], fill=couleur)

        #print("\n")



def nb_voisin (i,j):
        global ligne
        global colonne
        nb_voisin=0
        
        if M[i][(j+1)%colonne]!=0:
            nb_voisin+=1

        if M[i][(j-1+colonne)%colonne]!=0:
            nb_voisin+=1

        if M[(i+1)%ligne][(j-1+colonne)%colonne]!=0:
            nb_voisin+=1
        
        if M[(i+1)%ligne][j]!=0:
            nb_voisin+=1

        if M[(i+1)%ligne][(j+1)%colonne]!=0:
            nb_voisin+=1

        if M[(i-1+ligne)%ligne][(j-1+colonne)%colonne]!=0:
            nb_voisin+=1

        if M[(i-1+ligne)%ligne][j]!=0:
            nb_voisin+=1

        if M[(i-1+ligne)%ligne][(j+1)%colonne]!=0:
            nb_voisin+=1

        return nb_voisin

def nouvelle_generation():
        global ligne
        global colonne
        global t
        global M
        voisin=0
        vecteur=[]
        x=0
        y=0

        # calculer le damier de la nouvelle génération en appliquant les règles

        for i in range(ligne):
            vecteur.append([])
            for j in range (colonne):
                voisin=nb_voisin(i,j)
                if voisin==2:
                    vecteur[i].append(M[i][j])
                    continue
                if voisin==3:
                    vecteur[i].append(1)
                    continue
                vecteur[i].append(0)
        # copier le temp dans le principale        
        M=vecteur.copy()
        afficher_damier()
        global ID_nouvelle_generation
        ID_nouvelle_generation = fenetre.after(200, nouvelle_generation)



def arreter():
    fenetre.after_cancel(ID_nouvelle_generation)

def quitter():
    fenetre.destroy()


initialiser()

Initialiser = Button(fenetre, text="Initialiser", command=afficher_damier)
Initialiser.pack(side = LEFT)

Lancer = Button(fenetre, text="Lancer", command=nouvelle_generation)
Lancer.pack(side = LEFT)

Arreter = Button(fenetre, text="Arreter", command = arreter)
Arreter.pack(side = RIGHT)

Quitter = Button(fenetre, text="Quitter", command = quitter)
Quitter.pack(side = RIGHT)

Taille = Scale(fenetre, orient='horizontal', from_=0, to=100, resolution=1, length=50, label='Taille de la grille')
Taille.pack(side = TOP)

Vie = Scale(fenetre, orient='horizontal', from_=0, to=100, resolution=1, length=50, label='% de vie')
Vie.pack(side = TOP)

Vitesse = Scale(fenetre, orient='horizontal', from_=0, to=10, resolution=1, length=50, label='Vitesse')
Vitesse.pack(side = TOP)

#fenetre.after(500, life)
fenetre.mainloop()


#if __name__ == '__main__':
    #main()

# %%
