def data_urodzenia(pesel):
    dzien = pesel[4]+pesel[5]
    mies = int(pesel[2]+pesel[3])
    rok = pesel[0]+pesel[1]

    if mies>12:
        mies -= 20
        rok = '20' + str(rok)
    else:
        rok = '19' + str(rok)
    if mies<10:
            mies = str('0'+str(mies))
    return f'{rok}-{mies}-{dzien}'

with open('data.in', 'r') as file:
    for pesel in file:
        pesel = pesel.strip()
        print(data_urodzenia(pesel))