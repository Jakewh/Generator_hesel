import random

print("====PASGEN====\ngenerátor hesel\n===============")
mala_pismena = # vyzkoušet přidání ascii
#["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
velka_pismena = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
cisla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
znaky = ["/", "'", ":", ",", ".", ";", "<", ">", "~", "!", "@", "#", "$", "%", "^", "&", "*", "+", "=", "[", "]", "{", "}", "?", "-"]
delka_hesla = [8]

delka = int(input("Zadej požadovanou délku hesla: "))
delka_hesla.append(delka)
print("Zadej číslo požadovaného složení hesla:")
typ_hesla = int(input("1) Písmena, čísla i znaky\t2) Písmena a čísla\t3) Písmena\n"))
if typ_hesla == 1:
    heslo = random.choice(mala_pismena + velka_pismena + cisla + znaky), len(delka_hesla) # nevím jak udělat délku hesla!!
    print("Vaše heslo je:", heslo)
elif typ_hesla == 2:
        heslo = random.choice(mala_pismena + velka_pismena + cisla)
        print("Vaše heslo je:", heslo)
else:
    heslo = random.choice(mala_pismena + velka_pismena, delka)
    print("Vaše heslo je:", heslo)
print("Děkujeme za použití generátoru hesel. Stisknutím klávesy jej zavřete.")
input()
