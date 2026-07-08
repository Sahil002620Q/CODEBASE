#rather than
from time import time
list = [1,2,3,4,5,6]
sq_list = []
start = time()
for i in list :
    sq = i*i
    sq_list.append(sq)
end = time()
print(sq_list)
time_taken = end-start
print("time taken : ",time_taken)

start = time()
sqr = [i**2 for i in list ]
end = time()
time_taken = end-start
print(sqr)
print("time taken : ",time_taken)
