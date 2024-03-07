
from tabulate import tabulate
import random
import timeit

x_list = [20, 200, 2000, 20000, 200000, 2000000]
n_list = [1, 2, 3]

def particle_dancin(n,x):
    origin = []
    for i in range(n): 
        origin.append(0)
    position = list(origin)
    steps = [-1, 1]
    for i in range(x):
        position[random.randint(0, n-1)] += steps[random.randint(0, 1)]
        if position == origin:
            return True
    return False
    

def percent_func(n,x):
    counter = 0
    for i in range(100):
        if particle_dancin(n, x):
            counter += 1
    return str(counter) + "%"
        

def main():
    data = []
    temp = []
    time_list = ["d3 time(s)"]
    for n in n_list:
        temp = ["d" +str(n)]
        for x in x_list:
            num = percent_func(n,x)
            temp.append(num)
            if n == 3:
                stmt = "num = percent_func(3," + str(x) + ")"
                timer = timeit.Timer(stmt, "from __main__ import percent_func")
                func_time = timer.timeit(number=1)
                time_list.append(round(func_time, 2))
        data.append(temp)
    headers = ["dim", 20, 200, 2000, 20000, 200000, 2000000]
    data.append(time_list)
    table = tabulate(data, headers, tablefmt="grid")
    print(table)
    
main()
        