from tek import tek
from butun_sayilar import butun_sayilar
from asalsayibulma import asalsayibulma
sayilar2 = []
for x in butun_sayilar():
    sayilar2.append(x)
    if tek(x):
        print(x, "bir çift sayıdır.")
    else:
        print(x, "bir tek sayıdır.")

for y in sayilar2:
    if asalsayibulma(y):
        print(y,"Asal sayı değilidr")
    else:
        print(y,"Asal sayıdır.")
