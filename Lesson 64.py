#A Python program that reverses a list using two pointers, swapping values from the left and right ends and moving inward until the pointers meet.
def reverse_list_two_pointers(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
reverse_list_two_pointers(my_list)
print("Reversed list:", my_list)
#A Python program that rotates a list to the left by a chosen number of positions using slicing, then joins the shifted parts back together.
def rotate_left(lst, positions):
    if not lst:
        return lst
    shift = positions % len(lst)
    return lst[shift:] + lst[:shift]
my_list = [10, 20, 30, 40, 50]
n = 2
rotated_list = rotate_left(my_list, n)
print(f"Original list: {my_list}")
print(f"Rotated left by {n}: {rotated_list}")
#A Python program that reverses a list in fixed-size groups, flipping each chunk separately while keeping the overall group order the same.
def reverse_in_groups(lst, group_size):
    if group_size <= 1:
        return lst
    for i in range(0, len(lst), group_size):
        lst[i : i + group_size] = reversed(lst[i : i + group_size])
    return lst
numbers = [1,2,3,4,5,6,7,8]
k = 3
print("Original list:", numbers)
print("Reversed in groups:", reverse_in_groups(numbers, k))