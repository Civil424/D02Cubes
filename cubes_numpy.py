import numpy as np
import time 

start = time.time()

first_cube = np.random.randint(1,7,size=100000)
second_cube = np.random.randint(1,7,size=100000)

summ = first_cube + second_cube
more_than_7 = summ[summ >= 7]

size = more_than_7.size
final_probability = size/100_000
print(final_probability)

end = time.time()
print(end-start)