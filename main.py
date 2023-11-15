import random

class Atom:
    """Klass Atom som används för att skapa specifika instanser för varje atom i periodiskasystemet"""
    a_nummer_counter = 1
    def __init__(self, a_beteckning:str, a_vikt:float):
        """Init funktionen som skapar objekt utifrån klassen 'Atom'"""
        self.a_beteckning = a_beteckning
        self.a_vikt = a_vikt
        self.a_nummer = Atom.a_nummer_counter
        Atom.a_nummer_counter += 1

    def __str__(self):
        """Sträng funktionen som skrivet ut objektet"""
        return f"{self.a_nummer} {self.a_beteckning}: {self.a_vikt}"

class Periodiskasystemet:
    """Skapar en objekt utifrån klassen Periodiskasystemet"""
    def __init__(self):
        """Init funktionen som skapar en instans av klassen Periodiskasystemet"""
        self.a_lista = []
        self.a_dict = {}
    
    def visa_alla(self):
        """Skriver ut alla objekt is listan a_lista"""
        for atom in self.a_lista:
            print(atom)

    def las_fil(self):
        """Läser filen avikt och sparar innehållet """
        filnamn = "avikt.txt"
        fil = open(filnamn, "r")
        info = fil.readline().strip()
        while info:
            a_beteckning, a_vikt = info.split()
            ny_atom = Atom(a_beteckning, float(a_vikt))
            self.a_lista.append(ny_atom)
            info = fil.readline().strip()
        fil.close()
    
    def byt_plats(self):
        """Byter plats på värden i givna index"""
        platser = [(19,20), (28,29), (53,54), (91,92), (93,94)]

        for index1, index2 in platser:
            if 0 <= index1 < len(self.a_lista) and 0 <= index2 < len(self.a_lista):
                self.a_lista[index1], self.a_lista[index2] = self.a_lista[index2], self.a_lista[index1]

    def sortera(self):
        """Sorterar a_lista och ändrar på attributen a_nummer för objekten och fyller uppslagsverket a_dict"""
        self.a_lista.sort(key=lambda atom:atom.a_vikt, reverse=False)
        self.byt_plats()
        for i, atom in enumerate(self.a_lista, start =1):
            atom.a_nummer = i
        
        for atom in self.a_lista:
            self.a_dict[atom.a_nummer] = atom.a_beteckning

    def beteckning_quiz(self):
        random_key = random.choice(list(self.a_dict))
        random_beteckning = self.a_dict[random_key]
        val = input(f"Vilken atomnummer har atomen med beteckningen: {random_beteckning}")

    
    def nummer_quiz(self):
        """väljer och skriver ut en random key från a_dict"""
        random_nummer = random.choice(list(self.a_dict.keys()))
        print(f"Random key från a_dict: {random_nummer}")


def huvud_funktion():
    """Huvud funktionen av programmet"""
    p_table = Periodiskasystemet()
    p_table.las_fil()
    p_table.sortera()
    p_table.visa_alla()
    p_table.beteckning_quiz()
    p_table.nummer_quiz()

huvud_funktion()
