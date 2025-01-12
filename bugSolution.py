def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average}")

#Example of a list containing non-numbers
my_list_with_strings = [1,2,'a',4,5]
#This will throw an error because the sum function doesn't work on strings
#average = calculate_average(my_list_with_strings)
#print(f"The average is: {average}") 