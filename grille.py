"""
Fichier contenant la classe grille définissant une grille de jeu.
"""

class Grille :
    def __init__ (self, n):
        self.taille = n
        self.grille = []
        for i in range (n):
            self.grille.append([])
            for _ in range (n) : 
                self.grille[i].append(0)
    
    def afficher_grille(self):
        for ligne in range (self.taille):
            print()
            for col in range (self.taille):
                print (self.grille[ligne][col], end="")
        

grille = Grille(8) 
grille.afficher_grille()