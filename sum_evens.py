# Function to sum all even numbers in a list
def sum_evens(nums):
    # Default variable value for the sum result
    total = 0
   # Forloop to iterate through list
    for position in range(len(nums)):
        # Variable for "next" value in list
        x = nums[position]
        # If statement to determine if value is even
        if x % 2 == 0:
            # Variable for the even numbers cumulative sum
            total = int(total + x)
            # Variable to cause iteration through list
            position = position + 1
    return total


print(sum_evens([35, 34, 48, 36, 96, 11, 13, 20]))
