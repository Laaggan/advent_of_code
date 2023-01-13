data = list(map(int, open("2018/1_data.txt", "r").read().split("\n")))

summa = 0
siffror_sett = set()
i = 0

while True:
    summa = summa + data[i]

    if summa in siffror_sett:
        break

    siffror_sett.add(summa)
    i = (i + 1) % len(data)
    print(i)
    
print(summa)