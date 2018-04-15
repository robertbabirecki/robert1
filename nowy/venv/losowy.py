import random
import time
random.seed(time.time())
imiona=['papier','kamien','nozyce']
x=(random.choice(imiona))
print('podaj : papier ,kamien,nozyce')
y=input()
if x == y:
     print('jest remis')
if y == 'papier' and x == 'kamien':
    print('komputer wybrał:')
    print(x)
    print('wygrywsz')
if y == 'papier' and x == 'nozyce':
    print('komputer wybrał:')
    print(x)
    print('przegrywasz')
if y == 'kamien' and x == 'papier':
    print('komputer wybrał:')
    print(x)
    print('przegrywasz')
if y == 'kamien' and x == 'nozyce':
    print('komputer wybrał:')
    print(x)
    print('wygrywasz')
if y == 'nozyce' and x == 'papier':
    print('komputer wybrał:')
    print(x)
    print('wygrywasz')
if y == 'nozyce' and x == 'kamien':
    print('komputer wybrał:')
    print(x)
    print('przegrywasz')


