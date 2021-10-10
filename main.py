def is_Prime(x):
    '''
       determina daca un nr. este prim
       :param x: nr. intreg
       :return: True, daca x este prim sau False, in caz contrar
    '''
    if x < 2:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True

def test_is_Prime():
    assert is_Prime(5) is True
    assert is_Prime(20) is False
    assert is_Prime(17) is True

def toateNrsuntPrime(l):
    '''
    determina daca toate numerele dintr-o lista sunt prime
    :param l: lista de nr. intregi
    :return: True, daca toate numerele din l sunt prime, False, in caz contrar
    '''
    for x in l:
        if is_Prime(x) is False :
            return False
    return True

def test_toateNrsuntPrime():
    assert toateNrsuntPrime([11,15]) is False
    assert toateNrsuntPrime([2,3]) is True

def get_longest_all_primes(lst: list[int]) -> list[int]:
    '''
    determina cea mai lunga subsecventa de nr prime
    :param lst: lista cu nr intregi
    :return: returneaza cea mai lunga subsecventa de nr prime din lst
    '''
    subsecventaMax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if toateNrsuntPrime(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = lst[i:j + 1]
    return subsecventaMax

def test_get_longest_all_primes():
    assert get_longest_all_primes([11,3,5,7,4,3,5,6]) == [11,3,5,7]
    assert get_longest_all_primes([10,14,16,20]) == []
    assert get_longest_all_primes([11,15]) == [11]

def nr_div(x):
    '''
    dtermina numarul de divizori al unui numar
    :param x: numarul intreg
    :return: numarul de divizori al lui x
    '''
    nr=1 #consideram deja divizor pe insusi numarul
    for i in range (2, x//2):
        if x % i == 0:
            nr = nr+1
    return nr

def test_nrdiv():
    assert nr_div(12) == 4
    assert nr_div(25) == 2
    assert nr_div(10) == 2

def toateNrcuacelasiNrdiv(list):
    '''
    determina daca toate numerele dintr-o lista au acelasi numar de divizori
    :param list: lista cu numere intregi
    :return: True, daca toate numerele din l sunt au acelasi nr de divizori,iar False, in caz contrar
    '''
    div=nr_div(list[0])
    for x in list :
        if nr_div(x) != div:
            return False
    return True

def test_toateNrcuacelasiNrdiv():
    assert toateNrcuacelasiNrdiv([2,3,5,7]) is True

    assert toateNrcuacelasiNrdiv([6,2,8]) is False
    assert toateNrcuacelasiNrdiv([10,4]) is False


def get_longest_same_div_count(lst: list[int]) -> list[int]:
    '''
    determina cea mai lunga subsecventa de nr care au acelasi nr de divizor
    :param lst: lista cu nr intregi
    :return: returneaza cea mai lunga subsecventa de nr care respecta proprietatea din lst
    '''
    subsecventaMax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if toateNrcuacelasiNrdiv(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = lst[i:j + 1]
    return subsecventaMax

def test_get_longest_same_div_count():
  assert get_longest_same_div_count([16,20,12,7]) == [20,12]
  assert get_longest_same_div_count([16,11,13,15]) == [11,13]

def printMenu():
    print("1. Citire lista")
    print("2. Afisare cea mai lunga subsecventa in care toate numerele sunt prime")
    print("12. Afisare cea mai lunga subsecventa in care toate numerele au acelasi numri de divizori")
    print("x. Iesire")

def citireLista():
    l = []
    givenString = input("Dati lista, cu elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def main():
    l = []
    while True:
        printMenu()
        optiune = input("Alege optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
           print(get_longest_all_primes(l))
        elif optiune == "12":
            print(get_longest_same_div_count(l))
        elif optiune == "x":
            break
        else:
            print("Optiune invalida.")

if __name__ == "__main__":
    test_is_Prime()
    test_toateNrsuntPrime()
    test_get_longest_all_primes()
    test_nrdiv()
    test_toateNrcuacelasiNrdiv()
    test_get_longest_same_div_count()
    main()