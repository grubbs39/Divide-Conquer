import pandas as pd
import numpy as np 
import random

class mergesort:
    def mergeSort(data):
        if len(data) > 1:

            # Finding the mid of the array
            mid = len(data)//2

            # Dividing the array elements
            L = data[:mid]

            # into 2 halves
            R = data[mid:]

            # Sorting the first half
            mergesort.mergeSort(L)

            # Sorting the second half
            mergesort.mergeSort(R)

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    data[k] = L[i]
                    i += 1
                else:
                    data[k] = R[j]
                    j += 1
                k += 1

                # Checking if any element was left
            while i < len(L):
                data[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                data[k] = R[j]
                j += 1
                k += 1


    def main():

        nums = []

        for i in range(5):
            num = random.randint(0,50)
            nums.append(num)
        print("Here are the random numbers for Mergesort before the algorithim:")
        print(nums)

        mergesort.mergeSort(nums)

        print("Here are the random numbers sorted with Mergesort:")
        print(nums)

        """
        data = pd.read_excel("Divide_and_conquer_excel_sheet.xlsx")

        df1 = pd.DataFrame(data, columns = ['Array1'])
        df1.append(df1)
        #x = df1.to_numpy()
        arr = np.array([df1])

        print(arr)
        mergeSort(arr)
        print(arr)



        df2 = pd.DataFrame(data, columns = ['Array2'])
        arr2 = df2.to_numpy()
        print(arr2)
        mergeSort(arr2)
        print(arr2)



        data.to_excel(excel_writer = "Divide_and_conquer_excel_sheet_mergesort_output.xlsx")
        """