import numpy as np
import random as rd

def lengthCal(antPath,cities): # расчитывается расстояние
    length =[]
    dis = 0
    for i in range(len(antPath)):
        for j in range(len(antPath[i]) - 1):
            dis += cities[antPath[i][j]][antPath[i][j+1]]
        dis += cities[antPath[i][-1]][antPath[i][0]]
        length.append(dis)
        dis = 0
    return length

cities = np.array([
	[0, 5, 6],
	[5, 0, 7],
	[6, 7, 0]])

antNum = 3 # количество городов
alpha = 1 # фактор важности феромона
beta = 3 # фактор важности эвристической функции
pheEvaRate = 0.3 # скорость испарения феромона
cityNum = cities.shape[0]
pheromone = np.ones((cityNum,cityNum)) # феромоновая матрица
heuristic = 1 / (np.eye(cityNum) + cities) - np.eye(cityNum) # матрица эвристической информации

for i in range(1, 100):
    antPath = np.zeros((antNum, cityNum)).astype(int) - 1 # путь муравья
    firstCity = [i for i in range(3)]
    rd.shuffle(firstCity) # случайно назначается начальный город для каждого муравья
    unvisted = []
    p = []
    pAccum = 0

    for i in range(len(antPath)):
        antPath[i][0] = firstCity[i]

    for i in range(len(antPath[0]) - 1): # обновляется следующий город, в который собирается каждый муравей
        for j in range(len(antPath)):
            for k in range(cityNum):
                if k not in antPath[j]:
                    unvisted.append(k)

            for m in unvisted:
                pAccum += pheromone[antPath[j][i]][m] ** alpha * heuristic[antPath[j][i]][m] ** beta

            for n in unvisted:
                p.append(pheromone[antPath[j][i]][n] ** alpha * heuristic[antPath[j][i]][n] ** beta / pAccum)

            roulette = np.array(p).cumsum()
            r = rd.uniform(min(roulette), max(roulette))

            for x in range(len(roulette)):
                if roulette[x] >= r: # выбирается следующий город
                    antPath[j][i + 1] = unvisted[x]
                    break

            unvisted = []
            p = []
            pAccum = 0

    pheromone = (1 - pheEvaRate) * pheromone # феромон летучий
    length = lengthCal(antPath, cities)

    for i in range(len(antPath)):
        for j in range(len(antPath[i]) - 1):
            pheromone[antPath[i][j]][antPath[i][j + 1]] += 1 / length[i] # обновление феромона
        pheromone[antPath[i][-1]][antPath[i][0]] += 1 / length[i]

print(f'Кратчайший путь: {antPath[length.index(min(length))]} (Расстояние = {min(length)})')