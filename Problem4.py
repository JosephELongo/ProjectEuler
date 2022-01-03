#First try a brute force approach
#Create a palindrome checker: given a number n, return true if the number is the same forwards and backwards
#Then, run the function on all products of three digit numbers and store the max value
#The brute force method works, further optimizations can definitely be made
#Right now, many numbers are being double checked because of the nested for loop
#A better method would involve generatating three digit products in a different way

def isPalindrome(n):
    """
    Returns true if n is a palindromic number (it is the same number forwards and backwards) else returns false
    """
    return (str(n)) == (str(n)[::-1])

if __name__ == '__main__':
    max = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i*j
            if isPalindrome(product):
                if product > max:
                    max = product
    print(max)
