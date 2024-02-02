from random import random, shuffle, sample
from .utils.base import Base
from .utils.path import Path

class GA(Base):
    """
      `population: int` ЧИСЛО Особей
     Общее количество людей, участвующих в одной итерации.
     -----
      `iter: int` КОЛИЧЕСТВО ИТЕРАЦИЙ
     Максимальное количество итераций алгоритма.
     -----
      `s: float` КОЭФФИЦИЕНТ ВЫБОРА
     Определяет, сколько лучших особей попадут в следующую популяцию.
     -----
      `m: float` КОЭФФИЦИЕНТ МУТАЦИИ
     Определяет, как часто мутируют особи в популяции.
    """

    def __init__(self, population: int, iter: int, s: float, m: float) -> None:
        """Инициализирует гиперпараметры для алгоритма"""

        self.population = population
        self.iter = iter
        self.s = s
        self.m = m

    @staticmethod
    def __fitness_sort(dm: list[list[float]], individuals: list[list[int]]) -> None:
        """Сортирует особей данной популяции по подгонке"""

        individuals.sort(key=lambda i: GA._calculate_dist(dm, i))

    def __initialization(self, l: int) -> list[list[int]]:
        """Инициализирует первую популяцию особей"""

        base = list(range(l))
        individuals = []
        for _ in range(self.population):
            shuffle(base)
            individuals.append(base + [base[0]])
        return individuals

    def __selection(self, individuals: list[list[int]]) -> None:
        """Отбирает лучших особей из данной популяции"""

        del individuals[int(self.population * self.s) :]

    def __crossover(self, individuals: list[list[int]]) -> None:
        """Скрещивание некоторых особей данной популяции"""

        childs = []
        w_size = len(individuals[0]) // 2
        for _ in range(len(individuals), self.population):
            p1, p2 = sample(individuals, 2)
            childs.append(
                p1[: w_size - 1]
                + [i for i in p2[:-1] if i not in p1[: w_size - 1]]
                + [p1[0]]
            )
        individuals += childs

    def __mutation(self, individuals: list[list[int]]) -> None:
        """Мутирует некоторых особей данной популяции"""

        sampling = list(range(1, len(individuals[0]) - 1))
        for item in individuals:
            if random() < self.m:
                i, j = sample(sampling, 2)
                item[i], item[j] = item[j], item[i]

    def run(self, points: list[tuple[int]], name: str = None) -> Path:
        """Запускает алгоритм для заданных точек"""

        l = len(points)
        dm = GA._distance_matrix(points)
        individuals = self.__initialization(l)
        for _ in range(self.iter):
            GA.__fitness_sort(dm, individuals)
            self.__selection(individuals)
            self.__crossover(individuals)
            self.__mutation(individuals)
        GA.__fitness_sort(dm, individuals)
        return Path(indx=individuals[0], leng=GA._calculate_dist(dm, individuals[0]), name=name)


if __name__ == "__main__":
    pass