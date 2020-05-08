# Change log
# v2020.01.28

import numpy as np

var = 1
while var == 1:
    name = input("Digite o nome do arquivo: ")
    try:
        with open(name, 'r')as row:
            characters = row.read()
            separator = characters[309]
        if separator != ';':
            delimiters = ','
        else:
            characters = characters.replace(',', '.')
            with open(name, "w") as row:
                row.write(characters)
            delimiters = ';'
        var = 0
    except (IOError, OSError, NameError) as err:
        print(err, 'arquivo não encontrado!. Digite novamente')
        var = 1

all_data = np.loadtxt(name, delimiter=delimiters,
                      skiprows=4, usecols=(8, 4, 10, 11))

magnitude_and_phase_are_given = characters.find(
    'Impedance Magnitude (Ohms)') != -1

current_index = 0

current_temperature = 0
vector = []
for index in range(len(all_data)):
    temperature = all_data[index][0]
    if temperature != current_temperature:
        current_temperature = temperature
        vector.append(index)


vector.append(len(all_data) - 1)


for i in range(len(vector) - 2):
    matriz = all_data[vector[i]: vector[i+1], 1:4]
    if magnitude_and_phase_are_given:
        z_re = matriz[:, 1]*np.cos(matriz[:, 2])
        z_im = matriz[:, 1]*np.sin(matriz[:, 2])
        matriz[:, 1] = z_re
        matriz[:, -1] = z_im
        #print(all_data[vector[i]][0])
        np.savetxt(str(all_data[vector[i]][0])+'.txt', matriz, delimiter='  ')
    else:
        np.savetxt(str(all_data[vector[i]][0])+'.txt', matriz, delimiter='  ')
