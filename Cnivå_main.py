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
        self.meny()

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

    def nummer_quiz(self):
        """Quizzar användaren på atomnummer"""
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

            antal_input = 0
            while antal_input < 3:
                while True:
                    try:
                        val = int(input("Ditt val: "))
                        break
        
                    except ValueError:
                        print("Svara med 1, 2 eller 3!")
                if val == rätt_idx:
                    antal_input = 3
                    print("Korrekt svar!")
                elif val == 4:
                    self.meny()
                    break
                else:
                    antal_input += 1
                    chanser_kvar = 3-antal_input
                    print(f"Fel svar!\n Du har {chanser_kvar} försök kvar!")
                    continue
        

    def beteckning_quiz(self):
        """Quizzar användaren på atom beteckningar"""
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
            antal_input = 0
            while antal_input < 3:
                while True:
                    try:
                        val = int(input("Ditt val: "))
                        break
        
                    except ValueError:
                        print("Svara med 1, 2 eller 3!")
                if val == rätt_idx:
                    antal_input = 3
                    print("Korrekt svar!")
                elif val == 4:
                    self.meny()
                    break
                else:
                    antal_input += 1
                    chanser_kvar = 3-antal_input
                    print(f"Fel svar!\n Du har {chanser_kvar} försök kvar!")
                    continue

            


    def meny(self):
        """Main meny för användaren att navigera i programmet"""
        print("Hey och välkommen till denna program!")
        print("Du kan svara på allt inom programmet med 1, 2, 3, osv. och använda den för att öva på Periodiskasystemet!")
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
    p_table.meny()

def test():
    """Test funktion som används under debugging av programmet"""
    p_table = Periodiskasystemet()
    p_table.las_fil()
    p_table.sortera()
    p_table.visa_alla()
    p_table.meny()

#  test() <- Den kallar du för att testa specifika funktioner i programmet det är detta jag använder medans jag kodar

huvud_funktion()  #  <- Den kallar du för att köra programmet från användarens vypunkt
