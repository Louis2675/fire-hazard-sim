"""
Fichier contenant la classe grille définissant une grille de jeu.
"""
class Grille :
    def __init__ (self, taille):
        self.taille = taille
        self.grille = []
        for i in range (taille):
            self.grille.append([])
            for _ in range (taille) : 
                self.grille[i].append(0)
    
    def afficher_grille(self):
        for ligne in range (self.taille):
            print()
            for col in range (self.taille):
                print(self.grille[ligne][col], end="")
        

if __name__ == '__main__':
    grille = Grille(8) 
    grille.grille[2][3] = 1
    grille.afficher_grille()
    print()
    print(grille.grille[2][3])