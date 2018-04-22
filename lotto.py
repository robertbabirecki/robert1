import random
import time
random.seed(time.time())   #inicjalizacja  przypadkowego losowania (powiązanie z czasem)
TablicaLiczb=[]            #tworzenie tablicy liczb  od 1 do 49
for i in range(49):
    TablicaLiczb.append(int(i+1))
print('===========================================================================================')
print('                               SYMULATOR LOSOWAŃ LOTTO')
print('podaj sześć niepowtarzających się cyfr z zakresu od 1 do 49 oddzielonych od siebie spacjami')
print('===========================================================================================')
licznik=0                   #deklaracja zmiennej liczącej ilość powtorzonych liczb
PodaneLiczby = input()      #wprowadzenie ciągu znaków oddzielonych spacjami
print('Twoje liczby to :')  #wypisanie wprowadzonych znaków  na konsole
print(PodaneLiczby)
ListaLiczb=PodaneLiczby.split(" ")  #podzielenie ciągu znaków  spacjami
Liczby = []                         #deklaracja tablicy z int
for i in ListaLiczb:                #konwersja tablicy znaków  na tablice int
        Liczby.append(int(i))
        Liczby.sort()
if len(Liczby) != 6:                  #sprawdzenie  czy została wprowadzona poprawna ilość  liczb
         print('podałes niewłaściwa ilość liczb')
         print("podaj poprawną ilość :")
         WarunekA=0
else:
         WarunekA=1
for i in range(5):                   #sprawdzenie  czy liczby wprowadzone nie powtarzają się
    if Liczby[i] == Liczby[i+1]:
         print('Podałeś dwie takie same liczby')
         print('Podaj jeszcze raz poprawnie :')
         licznik=+1
if Liczby[0] < 1 or Liczby[5] > 49:         #sprawdzenie czy liczby s w zakresie od 1 do 49
    print('podałeś liczbe z poza  zakresu 1-49 ')
    print('Podaj jeszcze raz poprawnie :')
    WarunekC=0
else:
     WarunekC=1
if WarunekA==1 and licznik==0 and WarunekC==1:  #jesli wszystkie warunki są spełnione
        Wylosowane=random.sample(TablicaLiczb,6)  #losuje sześć liczb
        Wylosowane.sort()                          # sortujemy liczby wylosowane rosnąco (łądniej wyglda)
        print('Wylosowane zostały liczby :')        #wypisujemy wylosowane  przesortowane liczby
        print(Wylosowane)
        Wspolne=set(Liczby)&set(Wylosowane)       #sprawdzamy ile mamy wspólnyczliczb wprowadzonych i  wylosowanych
        print('liczby trafione to :')             #wypisujemy wspólne liczby   i  ilość liczb trafionych
        print(Wspolne)
        print('ilosc liczb trafionych to :')
        print(len(Wspolne))



