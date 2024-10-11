import sys


# Function to check if a number is a palindrome
def is_palindrome(n):
    original = n
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return original == reversed_n


# Function to reverse digits of a number without converting to string
def reverse_number(n):
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return reversed_n


# Function to apply the 196-algorithm and check for Lychrel numbers
def lychrel_test(n, max_iterations=500):
    iteration = 0
    while iteration < max_iterations:
        reversed_n = reverse_number(n)  # Reverse the digits of the number
        n += reversed_n
        iteration += 1

        if is_palindrome(n):
            return False, n, iteration  # Not a Lychrel number, palindrome found

    return True, n, iteration  # Possible Lychrel number (no palindrome found)


# Main function to test a range of numbers
def main():
    limit = 10000  # Set a limit for the range of numbers to check
    possible_lychrels = []

    for num in range(1, limit + 1):
        is_lychrel, result, iterations = lychrel_test(num)
        if is_lychrel:
            possible_lychrels.append(num)

    print(f"Possible Lychrel numbers up to {limit}: {possible_lychrels}")
    print(f"Number of possible Lychrel numbers: {len(possible_lychrels)}")


# Prevent recursion limit errors by setting a higher limit (use with caution)
sys.setrecursionlimit(2000)

if __name__ == "__main__":
    main()
