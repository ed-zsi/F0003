#F0003b: Bővítsd az előző programot úgy, hogy a kiírás előtt kérdezze meg a születési évedet és a csillagjegyedet, és az előző feladatban megadott mondat után ezt is közölje veled.

kenév = input('Mi a keresztneved?')
venév = input('Mi a vezetékneved?')
csjegy = input('Mi a csillagjegyed?')
szd = input('Mikor születtél?')
print('A te neved ', kenév, ' ', venév,'.', sep='')
print('A csillagjegyed a ', csjegy, sep='')
print(szd,'ban/ben születtél.',sep='-')