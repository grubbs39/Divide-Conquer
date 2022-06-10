import time
import random
from mergesort import mergesort
from Quicksort import Quicksort

print("Hello,")
print("We are going to be comparing some divide and concuer algorithims.")


start = time.perf_counter()
mergesort.main()
end = time.perf_counter()
print("Time consumed for Mergesort: ",end - start)


start = time.perf_counter()
Quicksort.main()
end = time.perf_counter()
print("Time consumed for Quicksort: ",end - start)


nums = []

for i in range(5):
    num = random.randint(0,50)
    nums.append(num)
print("Here are the random numbers for Quicksort before the algorithim together:")
print(nums)

start = time.perf_counter()
Quicksort.quicksort(0, len(nums)-1, nums)
end = time.perf_counter()

print("Here are the random numbers sorted with Quicksort together:")
print(nums)

print("Time consumed for Quicksort together: ",end - start)


print("Here are the random numbers for Mergesort before the algorithim together:")
print(nums)

start = time.perf_counter()
mergesort.mergeSort(nums)
end = time.perf_counter()

print("Here are the random numbers sorted with Mergesort together:")
print(nums)
print("Time consumed for Mergesort together: ",end - start)
