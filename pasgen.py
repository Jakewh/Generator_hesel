import random, string

print("====PASGEN====\ngenerátor hesel\n===============")
pismena = string.ascii_lowercase + string.ascii_uppercase   # importujeme malá i velká oísmena z ascii
cisla = string.digits   # importujeme čísla z ascii
znaky = string.punctuation  # importujeme znaky z ascii

print("Zadej typ požadovaného složení hesla:")
typ_hesla = int(input("1) Písmena, čísla i znaky\t2) Písmena a čísla\t3) Písmena\n"))   #volba typu hesla (1,2,3)
if typ_hesla == 1:
    for i in range(8):
        heslo = random.SystemRandom().choice(pismena + cisla + znaky)
        print("Vygenerované heslo je:", heslo)
elif typ_hesla == 2:
        heslo = random.SystemRandom().choice(pismena + cisla)
        print("Vygenerované heslo je:", heslo)
else:
    heslo = random.SystemRandom().choice(pismena)
    print("Vygenerované heslo je:", heslo)
print("Děkujeme za použití generátoru hesel. Stisknutím klávesy jej zavřete.")
input()
