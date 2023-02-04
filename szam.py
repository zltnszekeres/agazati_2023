import random
def oszthato_e():
    print('I/a')
    szam = random.randint(1,50)
    print(f'A generált szám: {szam}')
    print('I/b')
    eredmeny = ' '

    if szam % 3 == 0 or szam % 5 == 0:

        if szam % 3 != 0:

            eredmeny = 'A szám öttel osztható'

        elif szam % 5 != 0:

            eredmeny = 'A szám hárommal osztható '

        else:

            eredmeny = 'a szám hárommal és öttel is osztható'

    else:

        eredmeny = "  nincs megoldás"
    print(eredmeny)
