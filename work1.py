l2 = []
l3 = []

with open('cities2.txt', 'r', encoding='utf-8-sig') as f:
    l1 = f.readlines()
    for i in l1:
        i = i.strip().lower()
        l2.append(i.strip())

while True:
    a = input('Введите название города: ').lower()
    if a == 'lose':
        print('You are louser!!! ha ha...')
        break

    elif a not in l2 and a not in l3:
        print('Такого города нет')

    elif l3 == True and a[0] != l3[-1][-1]:
        print(f'Буква следующего города должна начинаться с -> {l3[-1][-1]}')

    elif a not in l2 and a in l3:
        print('Этот город уже было')

    elif a in l2:
        l3.append(l2.pop(l2.index(a)))
        for j in l2:
            if j.startswith(a[-1]):
                print(j)
                l3.append(l2.pop(l2.index(j)))
                break
        else:
            print('У меня закончился запас городов на эту букву. Ты выиграл!')
            break

print('\n')
print(f'Городо которые были использованы: {l3}')
