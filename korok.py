eletkor = []
def szambekeres ():

    i = 0;

    while i < 5:

        megadott_szam = int(input('Adj meg egy egész számot (összesen ötöt 0-120, között): '))


        eletkor.append(megadott_szam)

        i += 1


def kiiras ():

    i = 0
    szamsor = ' '

    while i < len(eletkor):

        szamsor += str(eletkor[i]) + ' : '





        i += 1
    print('II/a,b,c')
    print(f'{szamsor}{i}')
def elso_idos ():



    i = 0
    while i <= len(eletkor) and eletkor[i]<= 70:
        i += 1
    if i < len(eletkor):
        eletkor_index = i
    return eletkor_index
def konzolra_kiir():
    elso_index = elso_idos() + 1
    print(f'első idős ember korának helye a listában:  {elso_index}')



