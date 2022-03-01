import math
import statistics

arvot = input("Anna lista numeroita pilkulla eroteltuna:")

lista = arvot.split(",")
uusilista= []
for i in lista:
    uusilista.append(int(i))


print(min(uusilista))
print(max(uusilista))
print(statistics.mean(uusilista))
print(statistics.median(uusilista))
print(statistics.mode(uusilista))