"""
Simulating Rasch data
https://www.rasch.org/rmt/rmt213a.htm
"""

import random
from math import exp
import pandas as pd

random.seed(42)

class Item:
    def __init__(self, index):
        self.index = index
        self._difficulty = random.random()


    def get_difficulty(self):
        return self._difficulty

    def get_index(self):
        return self.index

    def set_difficulty(self, difficulty):
        self._difficulty = difficulty

class Test:
    def __init__(self, n):
        self.items = [Item(i) for i in range(n)]

    def get_difficulties(self):
        for i in self.items:
            yield i.get_index(), i.get_difficulty()

class Student:
    def __init__(self, name):
        self.name = name
        self._ability = random.normalvariate(0, 1)

    def take_test(self, test):
        names = []
        succeed = []
        for index, difficulty in test.get_difficulties():
            r = random.random()
            p_failure = 1/(1 + exp(self._ability - difficulty))
            succeed.append(1 if r > p_failure else 0)
            names.append(index)
        return names, succeed

    def get_ability(self):
        return self._ability

class Dataset:
    def __init__(self, class_size, total_items):
        self.test = Test(total_items)
        self.students = [Student(i) for i in range(class_size)]

    def get_dataset(self):

        ability = [s.get_ability() for s in self.students]
        results = [s.take_test(self.test) for s in self.students]
        grades = [succeed for _, succeed in results]

        return ability, grades


if __name__=='__main__':
    dataset = Dataset(10,5)
    ability, grades = dataset.get_dataset()
    df = pd.DataFrame(grades)
    df['ability'] = ability
    
    print(df)