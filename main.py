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

#samochody = ['syrena', 'polonez']
#ilosc = [3, 5]

#for s in samochody:
#    print(s)

#for il in ilosc:
#    print(s)


#gry = ['starcraft', 'wordcraft', 'overwatch']

#ilo = [2,6]

#print(len(ilosc))

#print("Dlugosc: {0}".format(len(samochody)))

#for idx in range(len(samochody)):
#    print ("idx" + str(idx) + ": " + samochody[idx])
#    print (samochody[idx] + " na ilosc dzwi " + str(ilosc[idx]))


#samolot = {'name' : 'boing', 'przebieg' : 1000 , 'type' : 'pasarzerski'}

#print(samolot['name'])
#for key, value in samolot.iteritems():
#    print("{0}:{1}".format(key,value))

#for key in samolot:
#    print("{0}:{1}, key, samolot[key]")


#pokemony = {'type' : 'ognisty', 'atak': 500, 'name' : 'Charmander' }

#print(pokemony['name'])
#for key, value in pokemony.iteritems():
#    print("{0}:{1}".format(key,value))

#for key in pokemony:
#    print("{0}:{1}, key, pokemony[key]")

def print_dict(d):
    for key, value in d.iteritems():
        print("{0}:{1}".format(key,value))

if __name__ == "__main__":
      samolot = {'name' : 'boing', 'przebieg' : 1000 , 'type' : 'pasarzerski'}

      print_dict(samolot)
      print_dict(samolot)
