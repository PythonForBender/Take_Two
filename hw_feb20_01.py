
dishes = int(input('Количество тарелок: '))
cleanser = int(input('Количество средства: '))
i = 0
clean = 0

while cleanser>0 and dishes>0:

    i = i + 1
    clean = clean + 1
    dishes = dishes - 1
    cleanser = cleanser - 0.5
    print(i,':','clean dishes: ', clean, ', dirty: ', dishes, ', средство: ',cleanser)


if cleanser == 0:
    print('dirty: ', dishes, ', средство: ',cleanser)
elif dishes == 0:
    print('dirty: ', dishes, ', средство: ',cleanser)
else:
    print('error')






















