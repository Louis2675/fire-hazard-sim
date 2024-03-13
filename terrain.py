"""
Fichier contenant la classe grille définissant une grille de jeu.
"""

class Parcelle:
    def __init__(self, type_terrain, est_maison, intensite_feu):
        self.type_terrain = type_terrain
        self.est_maison = est_maison
        self.intensite_feu = intensite_feu


class Terrain:
    def __init__ (self, taille):
        self.taille = taille
        self.grille = []
        for i in range (taille):
            self.grille.append([])
            for _ in range (taille) : 
                self.grille[i].append(Parcelle("None", False, 0))
    
    def afficher_grille(self):
        for ligne in range(self.taille):
            print()
            for col in range(self.taille):
                parcelle = self.grille[ligne][col]
                if isinstance(parcelle, Parcelle):
                    print("[{}, {}, {}]".format(parcelle.type_terrain, parcelle.est_maison, parcelle.intensite_feu), end="")
                else:
                    print("[Error: not a Parcelle instance]", end="")

if __name__ == '__main__':
    grille = Terrain(8) 
    grille.grille[2][3] = 1
    grille.afficher_grille()
