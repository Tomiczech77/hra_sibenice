from random import choice

def ano_nebo_ne(otazka):
    """Vrátí True nebo False podle odpovědi uživatele"""
    while True:
        odpoved = input(otazka).lower().strip()
        if odpoved == 'ano':
            return True
        elif odpoved == 'ne':
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne".')

def obrazek(level):
    if level == 0:
        return """






        ~~~~~~~
        """
    elif level == 1:
        return """
        +
        |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 2:
        return """
        +---.
        |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 3:
        return """
        +---.
        |   |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 4:
        return """
        +---.
        |   |
        |   O
        |
        |
        |
        ~~~~~~~
        """
    elif level == 5:
        return """
        +---.
        |   |
        |   O
        |   |
        |
        |
        ~~~~~~~
        """
    elif level == 6:
        return """
        +---.
        |   |
        |   O
        | --|
        |
        |
        ~~~~~~~
        """
    elif level == 7:
        return """
        +---.
        |   |
        |   O
        | --|--
        |
        |
        ~~~~~~~
        """
    elif level == 8:
        return """
        +---.
        |   |
        |   O
        | --|--
        |  /
        |
        ~~~~~~~
        """
    else:
        return """
        +---.
        |   |
        |   O
        | --|--
        |  / \\
        |
        ~~~~~~~
        """

def zamen(slovo, index, znak):
    """Ve slově zamění znak na určité pozici."""
    zacatek_slova = slovo[:index]
    konec_slova = slovo[index + 1:]
    nove_slovo = zacatek_slova + znak + konec_slova
    return nove_slovo

def vyber_slova():
    """vybere z několika slov jedno slovo"""
    with open("slova.txt", encoding="utf-8") as slova:
        seznam = []
        for slovo in slova:
            seznam.append(slovo.strip())
        return choice(seznam)

def hra_sibenice():
    """Hra šibenice"""
    nepovolene_znaky = '!"#$%&\'()*+,-./:;<=>?@[\]^{|}~_\n '
    slovo = vyber_slova()
    hadane_slovo = "_" * len(slovo)
    print(f"Uhádni slovo: {hadane_slovo}.")

    pocet_neuspesnych_pokusu = 0
    print(obrazek(pocet_neuspesnych_pokusu))

    while True:
        pismeno = input("Napiš písmeno: ").strip().lower()
        misto = 0
        
        if len(pismeno) != 1:
                    print("Je potřeba napsat přesně 1 písmeno...")
                    print(obrazek(pocet_neuspesnych_pokusu))

        elif pismeno in nepovolene_znaky:
            print("Potřebuji pouze písmeno...")

        elif pismeno in slovo:
            pocet_opakovani = slovo.count(pismeno)
            for i in range(pocet_opakovani):
                pozice = slovo.index(pismeno, misto)
                misto = pozice + 1
                hadane_slovo = zamen(hadane_slovo, pozice, pismeno)
            
        else:
            pocet_neuspesnych_pokusu += 1
            print("Písmeno není ve slově.")
            print(obrazek(pocet_neuspesnych_pokusu))
            
        
        print(pocet_neuspesnych_pokusu)
        
        
        print(hadane_slovo)

        if "_" not in hadane_slovo:
            print(f"Gratuluji, dokončil jsi hru. Hledané slovo bylo: {slovo}")
            break

        print(f"Počet neúspěšných pokusů: {pocet_neuspesnych_pokusu}")

        if pocet_neuspesnych_pokusu >= 9:
            print(f'Prohrál jsi. Až moc pokusů. Třeba budeš mít štěstí příště. Hledané slovo bylo: "{slovo}".')
            break

while True:
    print("HRA ŠIBENICE")
    hra_sibenice()
    pokracovani_hry = ano_nebo_ne("Zkusíš si zahrát znovu? ")
    if not pokracovani_hry:
        break

print("KONEC HRY.")