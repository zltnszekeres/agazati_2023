import osztaly

def beolvas():
    file = open('gombak_jav.txt', 'r', encoding='utf-8')

    file.readline()

    gombak = []

    for sor in file:
        sorertekek = sor.strip().split('@')
        gomba = osztaly.Gomba(sorertekek[0].strip(), sorertekek[1].strip(), sorertekek[2].strip())
        gombak.append(gomba)


    return gombak
def gombakszama(gombak):
    print('III/a, b')
    print(f'\tA gombák száma: {len(gombak)}.')

def kiir():
    gombak = beolvas()
    gombakszama(gombak)






