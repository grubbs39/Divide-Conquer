import random

class Quicksort:
    def partition(l, r, nums):
        # Last element will be the pivot and the first element the pointer
        pivot, ptr = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                # Swapping values smaller than the pivot to the front
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        # Finally swapping the last element with the pointer indexed number
        nums[ptr], nums[r] = nums[r], nums[ptr]
        return ptr

    # With quicksort() function, we will be utilizing the above code to obtain the pointer
    # at which the left values are all smaller than the number at pointer index and vice versa
    # for the right values.


    def quicksort(l, r, nums):
        if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
            return nums
        if l < r:
            pi = Quicksort.partition(l, r, nums)
            Quicksort.quicksort(l, pi-1, nums)  # Recursively sorting the left values
            Quicksort.quicksort(pi+1, r, nums)  # Recursively sorting the right values
        return nums



    def main():

        nums = []

        for i in range(5):
            num = random.randint(0,50)
            nums.append(num)
        print("Here are the random numbers for Quicksort before the algorithim:")
        print(nums)

        Quicksort.quicksort(0, len(nums)-1, nums)

        print("Here are the random numbers sorted with Quicksort:")
        print(nums)

        """
        data = pd.read_excel("Divide_and_conquer_excel_sheet.xlsx")

        df1 = pd.DataFrame(data, columns = ['Array1'])
        arr = df1.to_numpy()
        print(arr)
        quicksort(0, len(arr)-1, arr)
        print(arr)


        df2 = pd.DataFrame(data, columns = ['Array2'])
        arr2 = df2.to_numpy()
        print(arr2)
        quicksort(0, len(arr2)-1, arr2)
        print(arr2)

        data.to_excel(excel_writer = "Divide_and_conquer_excel_sheet_Quicksort_output.xlsx")
        """