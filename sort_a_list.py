########################################################################################################################
# Problem Statement : Write a function that sorts a list of numbers in ascending order.                                #
########################################################################################################################
# I've used the bubble sorting algorithm, the basic idea is that in each iteration, it checks for the adjacent number  #
# and swaps the number if the adjacent number is lesser than the previous. This continues till n iterations where n is #
# the size of the list. However, inefficient because the list can be presorted or sorted before the n iterations.      #
########################################################################################################################

# sorts the list in an ascending order using Bubble sort
def bubble_sort(the_list):
    # obtain the length of the list
    n = len(the_list)
    # perform n-1 iterations on the entire list
    for i in range(n-1, 0, -1):
        # for each iteration, move the largest item to the end
        for j in range(i):
            if the_list[j] > the_list[j+1]:
                # swap if two adjacent items are out of order
                the_list[j], the_list[j + 1] = the_list[j + 1], the_list[j]
    return the_list

data = [33,20,99,4,45,19,77,63]

print("The list to be sorted : " , data)
print("The sorted list in ascending format: " , bubble_sort(data))

# Testing Cases

# Passing an empty list
data = []
print("The list to be sorted : " , data)
print("The sorted list in ascending format: " , bubble_sort(data))

# Passing a list with floats and whole numbers
data = [0.3,4.3,4,42,2,4,444]
print("The list to be sorted : " , data)
print("The sorted list in ascending format: " , bubble_sort(data))

# Passing a list with large values and zero
data = [10000,4000,20,3004,0,3244,9]
print("The list to be sorted : " , data)
print("The sorted list in ascending format: " , bubble_sort(data))

"""

In Bubble Sort, n-1 comparisons will be done in the 1st pass, n-2 in 2nd pass, n-3 in 3rd pass and so on. 
So the total number of comparisons will be,

(n-1) + (n-2) + (n-3) + ..... + 3 + 2 + 1
Sum = n(n-1)/2
i.e O(n2)

Also, the best case time complexity will be O(n), it is when the list is already sorted.

Best Case : O(n)
Average Case: O(n^2)
Worst Case: O(n^2)

"""