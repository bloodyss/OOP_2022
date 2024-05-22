import random
x=1
y=0
def f1(mass, K):
    for i in range(len(mass)):
        for j in range(i + 1, len(mass)):
            if mass[i] + mass[j] == K:
                return [mass[i], mass[j]]
    return -1
N = int(input("Введите размер массива: "))
while x==1:
    mass = sorted([random.randint(1, 100) for i in range(N)])
    print([mass])
    K = random.randint(1, 100)
    print("Число К=",K)
    res = f1(mass, K)

    if res != -1:
        print("Массив чисел сумма = К")
        print(res[0],res[1])
        print("сумма(или число К)= ")
        print(K)
        x=2
        y+=1
    else:
        print("-1")
        y+=1

print("Количество попыток",y)