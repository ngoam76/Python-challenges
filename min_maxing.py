def largest_difference(list_of_number):
    max1 = max(list_of_number)
    min1 = min(list_of_number)
    difference = max1 - min1
    print(difference)
    return difference

largest_difference([1,7,10,55,90])