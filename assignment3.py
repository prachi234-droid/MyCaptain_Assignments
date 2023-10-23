def print_positive_numbers(list_numbers):
    positive_numbers = [num for num in list_numbers if num > 0]
    return positive_numbers

n = int(input("Enter the number of elements in the list: "))
list_numbers = list(map(int, input("Enter the list of numbers: ").strip().split()))[:n]

positive_numbers = print_positive_numbers(list_numbers)
print("Positive numbers in the list are:", positive_numbers)
