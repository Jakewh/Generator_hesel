"""
Program pro generování hesla
"""

import random, string

print("""                                  
 _ __   __ _ ___  __ _  ___ _ __  
| '_ \ / _` / __|/ _` |/ _ \ '_ \ 
| |_) | (_| \__ \ (_| |  __/ | | |
| .__/ \__,_|___/\__, |\___|_| |_|
|_|              |___/            
""")


pismena = list(string.ascii_lowercase + string.ascii_uppercase) # importujeme malá i velká oísmena z ascii
cisla = list(string.digits)   # importujeme čísla z ascii
znaky = list(string.punctuation)  # importujeme znaky z ascii
heslo = []
delka = int(input("Zadejte požadovanou délku hesla: "))

print("Zadej typ požadovaného složení hesla:")
typ_hesla = int(input("1) Písmena, čísla i znaky\t2) Písmena a čísla\t3) Písmena\n"))   # volba typu hesla (1,2,3)

# volba písmena, čísla i znaky
if typ_hesla == 1:
    if delka >= 3:
        while len(heslo) < delka:
                znak = random.SystemRandom().choice(pismena)
                heslo.append(znak)
                znak = random.SystemRandom().choice(cisla)
                heslo.append(znak)
                znak = random.SystemRandom().choice(znaky)
                heslo.append(znak)
    else:
        print("Délka hesla je pro požadovaný typ moc krátká")

# volba písmena a čísla
elif typ_hesla == 2:
    if delka >= 2:
        while len(heslo) < delka:
                znak = random.SystemRandom().choice(pismena)
                heslo.append(znak)
                znak = random.SystemRandom().choice(cisla)
                heslo.append(znak)

# volba písmena
elif typ_hesla == 3:
    for i in range(delka):
        znak = random.SystemRandom().choice(pismena)
        heslo.append(znak)

random.shuffle(heslo)
if len(heslo) > 0:
    print("Vygenerované heslo je:", "".join(heslo))
print("""
Děkujeme za použití generátoru hesel. Stisknutím klávesy jej zavřete.
***Hacker Ninjas North 2022***
""")
input()
