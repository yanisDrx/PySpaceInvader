
class EtreVivant():
    ESPECE_ETRE_VIVANT = "(etre vivant non identifié)"
    def DonnerEspece(self):
        print(self.ESPECE_ETRE_VIVANT)
        
    def sePresenter(self):
        if self.age != 0:
            print(f"Bonjour je m'appelle {self.nom} j'ai {self.age} ans.")
        else:
            print(f"Bonjour je m'appelle {self.nom}.") 
        
class Chat(EtreVivant):
    ESPECE_ETRE_VIVANT = "Chat (mammifère félin)"
    
    def __init__(self,nom,age):
        
        self.nom = nom
        self.age = age

class Personne(EtreVivant):
    ESPECE_ETRE_VIVANT = "Humain (mammifère)"
    def __init__(self, nom: str = "", age: int = 0):
        
        self.nom = nom
        self.age = age
        
        # if len(self.nom) == 0:
        #     self.demanderNom()
            
        # if self.age == 0:
            # self.demanderAge()
            
        # print(f"Constructeur personne {self.nom}")
        
        
    def estMajeur(self):
        return self.age >= 18
    
    def demanderNom(self):
        self.nom = input("Veuillez entrer votre nom : ")
        return self.nom
    
    def sePresenter(self):
        return super().sePresenter(),print(f"Je suis {'majeur' if self.estMajeur() else 'mineur'}")

    
    # def demanderAge(self):
    #     self.age = int(input("Veuillez entrer votre age : "))
    #     return self.age

liste_personnes = [Personne('Yanis',17)]

chat = Chat('Chaussette', 7)
chat.sePresenter()
chat.DonnerEspece()

for personnes in liste_personnes:
    personnes.sePresenter()
    personnes.estMajeur()
    personnes.DonnerEspece()

# personne1.sePresenter()
# personne2.sePresenter()

# personne1 = Personne('Yanis',18)    
# personne2 = Personne('Rayane',20)
print()
