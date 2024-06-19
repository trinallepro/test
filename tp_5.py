#############
# Import(s) #
#############
from p5 import *
from random import randrange

######################
# Variables globales #
######################

# La fenêtre
LARGEUR = 1920
HAUTEUR = 1280
# Les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (50, 50, 50)

####################################
# Fonctions exécutées au lancement #
####################################
def setup():
    size(LARGEUR, HAUTEUR)
    
    # Décommenter pour modifier la bordure des figures
    # stroke_weight(10)
    no_stroke()
    # stroke(*BLANC)
    


def draw():
    # Le fond
    background(*BLANC)
    l=10
    g=10
    for x in range(0,LARGEUR,100):
        for y in range(0,HAUTEUR,100):
            r = randrange(0,256)
            g = randrange(0,256)
            b = randrange(0,256)
            fill(r,g,b)
            rect(x,y,l,g)

    # Votre code
    #rd = randrange(0,256)
    #gd = randrange(0,256)
    #bd = randrange(0,256)
    #ra = randrange(0,256)
    #ga = randrange(0,256)
    #ba = randrange(0,256)
    #for x in range(0,LARGEUR,1):
     #   r =int((ra-rd)/LARGEUR * x + rd)
      #  g =int((ga-gd)/LARGEUR* x + gd)
      #  b =int((ba-bd)/LARGEUR* x + bd)
      #  fill(r,g,b)
      #  rect(x,0,1,HAUTEUR)
    #save_frame("essai.png")
      
     

##########################
run()
