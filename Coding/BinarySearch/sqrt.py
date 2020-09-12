# Intuition : The sqrt is never greater than the half of it's value 
# Base case : If the number is less than 2 then the sqrt is itself

def sqrt(num):
    if num < 2:
        return num

    left = 2
    right = num // 2

    while left <= right: 
        mid = left + ( right - left ) // 2 
        potentialMatch = mid * mid 
        if potentialMatch == num:
            return mid 
        elif potentialMatch > num:
            right = mid - 1
        else: 
            left = mid + 1 
        
    return right


if __name__ == '__main__':

    print(sqrt(6))

