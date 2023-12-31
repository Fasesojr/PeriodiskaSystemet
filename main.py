import random

class Atom:
    """Klass Atom som används för att skapa specifika instanser för varje atom i periodiskasystemet"""
    a_nummer_counter = 1
    def __init__(self, a_beteckning:str, a_vikt:float):
        """Init funktionen som skapar objekt utifrån klassen 'Atom'"""
        self.a_beteckning = a_beteckning
        self.a_vikt = a_vikt
        self.a_nummer = 0

    def __str__(self):
        """Sträng funktionen som skrivet ut objektet"""
        return f"{self.a_nummer} {self.a_beteckning}: {self.a_vikt}"

class Periodiskasystemet:
    """Skapar en objekt utifrån klassen Periodiskasystemet"""
    def __init__(self):
        """Init funktionen som skapar en instans av klassen Periodiskasystemet"""
        self.a_lista = []
        self.a_dict = {}
        self.p_matris = [[None] * 18 for _ in range(9)]
    
    def visa_alla(self):
        """Skriver ut alla objekt is listan a_lista"""
        for atom in self.a_lista:
            print(atom)

        #  Printa PeriodiskaSystemet
        header = f"{'': <5}{'     '.join(map(str,range(1,19))): >4}"
        print(header)

        for i, row in enumerate(self.p_matris, start=1):
            row_str=f"{i: <5}"
            for j, element in enumerate(row, start=1):
                if element:
                    row_str += f"{element.a_nummer}:{element.a_beteckning:<3}"
                else:
                    row_str += "      "
            print(row_str)
        #self.meny()

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
        platser = [(17,18), (26,27), (51,52), (89,90), (91,92)]

        for index1, index2 in platser:
            if 0 <= index1 < len(self.a_lista) and 0 <= index2 < len(self.a_lista):
                self.a_lista[index1], self.a_lista[index2] = self.a_lista[index2], self.a_lista[index1]

    def sortera_matris(self):
        """Sorterar formaten av matrisen och fyller"""
        self.p_matris = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
    ]
        atom_index = 0
        for i, row in enumerate(self.p_matris):
            for j, value in enumerate(row):
                if value == 1:
                    if 58 <= atom_index < 72 and atom_index < len(self.a_lista):
                        self.p_matris[7][j] = self.a_lista[atom_index]
                    elif 89 <= atom_index < 102 and atom_index < len(self.a_lista):
                        self.p_matris[8][j] = self.a_lista[atom_index]
                    elif atom_index < len(self.a_lista):
                        self.p_matris[i][j] = self.a_lista[atom_index]
                    else:
                        self.p_matris[i][j] = None
                    atom_index += 1
                else:
                    self.p_matris[i][j] = None


    def sortera(self):
        """Sorterar a_lista och ändrar på attributen a_nummer för objekten och fyller uppslagsverket a_dict och matrisen p_matris"""
        self.a_lista.sort(key=lambda atom:atom.a_vikt, reverse=False)
        self.byt_plats()
        for i, atom in enumerate(self.a_lista, start =1):
            atom.a_nummer = i
    
        for atom in self.a_lista:
            self.a_dict[atom.a_nummer] = atom.a_beteckning
        
        self.sortera_matris()

    

    def nummer_quiz(self):
        while True:
            random_key = random.choice(list(self.a_dict))
            random_beteckning = self.a_dict[random_key]
            print(f"Vilken atomnummer har atomen med beteckningen: {random_beteckning}")
        
            rätt_svar = random_key
            svars_alternativ = list(self.a_dict.keys())
            random.shuffle(svars_alternativ)
            svars_alternativ = svars_alternativ[:2]
            svars_alternativ.append(rätt_svar)
            random.shuffle(svars_alternativ)
            for idx, alternativ in enumerate(svars_alternativ, start=1):
                print(f"{idx}. {alternativ}")
            print("4. Tillbaka till menyn")
            rätt_idx = svars_alternativ.index(rätt_svar) + 1

            while True:
                try:
                    val = int(input("Ditt val: "))
                    break
        
                except ValueError:
                    print("Svara med 1, 2 eller 3!")
        
            if val == rätt_idx:
                print("Korrekt svar!")
            elif val == 4:
                self.meny()
                break
            else:
                print("Fel svar!")
        

    def beteckning_quiz(self):
        """väljer och skriver ut en random key från a_dict"""
        while True:
            random_nummer = random.choice(list(self.a_dict.keys()))
            print(f"Vilken beteckning har atomen med atomnummer: {random_nummer}")

            rätt_svar = self.a_dict[random_nummer]
            svars_alternativ = list(self.a_dict.values())
            random.shuffle(svars_alternativ)
            svars_alternativ = svars_alternativ[:2]
            svars_alternativ.append(rätt_svar)
            random.shuffle(svars_alternativ)
            for idx, alternativ in enumerate(svars_alternativ, start=1):
                print(f"{idx}. {alternativ}")
            print("4. Tillbaka till menyn")
            rätt_idx = svars_alternativ.index(rätt_svar) + 1

            while True:
                try:
                    val = int(input("Ditt val: "))
                    break
        
                except ValueError:
                    print("Svara med 1, 2 eller 3!")
            if val == rätt_idx:
                print("Korrekt svar!")
            elif val == 4:
                self.meny()
                break
            else:
                print("Fel svar!")

    def meny(self):
        """Main meny för användaren att navigera i programmet"""
        while True:
            try:
                val = int(input("------ Meny ------\n1. Visa Periodiskasystemet\n2. Träna på atomnummer\n3. Träna på atombeteckningar\n4. Avsulta programmer\nVal: "))
                if val == 1:
                    self.visa_alla()
                    break
                elif val == 2:
                    self.nummer_quiz()
                    break
                elif val == 3:
                    self.beteckning_quiz()
                    break
                elif val == 4:
                    print("Avslutar programmet. ")
                    exit()
                else:
                    print("Var snäll och svara med 1, 2, 3 eller 4\nVal: ")
            except ValueError:
                print("Var snäll och svara med 1, 2, 3 eller 4\nVal: ")

def huvud_funktion():
    """Huvud funktionen av programmet"""
    p_table = Periodiskasystemet()
    p_table.las_fil()
    p_table.sortera()
    p_table.visa_alla()
    p_table.beteckning_quiz()
    p_table.nummer_quiz()

def main():
    GUI1.main()

def test():
    """Test funktion som används under debugging av programmet"""
    p_table = Periodiskasystemet()
    p_table.las_fil()
    p_table.sortera()
    p_table.visa_alla()
    

test()