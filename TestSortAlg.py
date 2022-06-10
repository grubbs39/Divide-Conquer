import time
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

