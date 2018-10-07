# Program liczczy
#markasamochodu =input('Wpisz marke: ')
#ilosc_aut = input('Ilosc aut: ')
#cena = input('Cena: ')
#rata = input('Rata: ')


#print("Auto" + " " + markasamochodu.upper() + " " +  markasamochodu.lower() + " " +  str(ilosc_aut) );

#Obliczenia
#if ilosc_aut > 5:
#    calosc = cena * rata
#    print "To jest super" + str(calosc)
#else:
#    print "Ojej"

samochody = ['syrena', 'polonez']
ilosc = [3, 5]

#for s in samochody:
#    print(s)

#for il in ilosc:
#    print(s)


#gry = ['starcraft', 'wordcraft', 'overwatch']

#ilo = [2,6]

#print(len(ilosc))

print("Dlugosc: {0}".format(len(samochody)))

for idx in range(len(samochody)):
    print ("idx" + str(idx) + ": " + samochody[idx])
    print (samochody[idx] + " na ilosc dzwi " + str(ilosc[idx]))
