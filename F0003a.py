#F0003a: Írj programot, amely külön-külön megkérdi a vezeték- és a keresztneved, majd kiírja őket egy mondatban, pl: A te neved Kovács Boldizsár. (A pontot se felejtsd el!)

kenév = input('Mi a keresztneved?')
venév = input('Mi a vezetékneved?')
print('A te neved ', kenév, ' ', venév,'.', sep='')