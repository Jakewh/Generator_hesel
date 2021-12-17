"Program pro generování hesla"

import random, string

class color:    # barva nadpisu
    RED = "\033[91m"
    END = "\033[0m"

pismena = string.ascii_lowercase + string.ascii_uppercase   # importujeme malá i velká oísmena z ascii
cisla = string.digits   # importujeme čísla z ascii
znaky = string.punctuation  # importujeme znaky z ascii
delka = int(input("Zadejte požadovanou délku hesla: "))

print("Zadej typ požadovaného složení hesla:")
typ_hesla = int(input("1) Písmena, čísla i znaky\t2) Písmena a čísla\t3) Písmena\n"))   # volba typu hesla (1,2,3)
if typ_hesla == 1:
    heslo = "".join(random.SystemRandom().choice(pismena + cisla + znaky)) # pojebaná délka hesla pořád nejde
    print("Vygenerované heslo je:", heslo)
elif typ_hesla == 2:
        heslo = "".join(random.SystemRandom().choice(pismena + cisla))
        print("Vygenerované heslo je:", heslo)
else:
    heslo = "".join(random.SystemRandom().choice(pismena))
    print("Vygenerované heslo je:", heslo)
print("Děkujeme za použití generátoru hesel. Stisknutím klávesy jej zavřete.")
input()
