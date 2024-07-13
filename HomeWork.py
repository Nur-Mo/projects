if __name__ == '__main__':
    x = int(input("Enter any number: "))
    y = int(input("Enter any number: "))
    z = int(input("Enter any number: "))
    n = int(input("Enter any number: "))

    # Using list comprehension to generate the coordinates
coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]

print(coordinates)
print("-"*50)

def pyfunc(r):
    for x in range(r):
        print(''*(r-x-1)+'*'*(2*x+1))
x = 10
pyfunc(x)
print(type(x),id(x))
print("-"*50)

# Write a program for binary search.
def BinarySearch(lys, val):
    first = 0  # Index of the first element in the array
    last = len(lys) - 1  # Index of the last element in the array
    index = -1  # Initialize the variable to store the index of the target value, initially set to -1 indicating not found

    # Loop until the first index is less than or equal to the last index and the target value is not found (index remains -1)
    while first <= last and index == -1:
        mid = (first + last) // 2  # Calculate the midpoint of the current search interval

        # If the value at the midpoint is equal to the target value, update the index to the midpoint
        if lys[mid] == val:
            index = mid
        else:
            # If the target value is less than the value at the midpoint, update the last index to search the left half
            if val < lys[mid]:
                last = mid - 1
            # If the target value is greater than the value at the midpoint, update the first index to search the right half
            else:
                first = mid + 1

    return index  # Return the index of the target value if found, otherwise -1
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Define the value to search for
target_value = int(input("Enter the value you're looking for: "))

# Call the BinarySearch function
result_index = BinarySearch(my_list, target_value)

# Check if the value was found or not
if result_index != -1:
    print(f"The value {target_value} was found at index {result_index}.")
else:
    print(f"The value {target_value} was not found in the list.")
print("-"*50)

# Write a program for interpolation search
def InterpolationSerach(lys, val):
    low = 0
    high = (len(lys)-1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((format(high - low)/(lys[high] - lys[low])) * (val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1
        else:
            high = index - 1
    return - 1

my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Define the value to search for
target_value = int(input("Enter the value you're looking for: "))

# Call the BinarySearch function
result_index = BinarySearch(my_list, target_value)

# Check if the value was found or not
if result_index != -1:
    print(f"The value {target_value} was found at index {result_index}.")
else:
    print(f"The value {target_value} was not found in the list.")
print("-"*50)
