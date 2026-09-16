import numpy as np
import time

def cube():
    mass = []
    for i in range(100_000):
        value = np.random.randint(1,7)
        mass.append(value)
    return mass

def sum_of_lists(list1, list2):
    summ = []
    for i in range(100_000):
        summ.append(list1[i] + list2[i])
    return summ

def search_more_than_7(mass):
    num = 0
    for i in range(100_000):
        if mass[i] >= 7:
            num += 1
    return num

start = time.time()

first_cube = cube()
second_cube = cube()

summ = sum_of_lists(first_cube,second_cube)

more_than_7 = search_more_than_7(summ)
size = more_than_7
final_probability = size/100_000
print(final_probability)

end = time.time()
print(end-start)