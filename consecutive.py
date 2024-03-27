
#Task 1 Find missing consecutive number 

def find_missing_number(numbers):
    n = len(numbers) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    missing_number = total_sum - actual_sum
    return missing_number

def main():
    numbers = []
    print("Enter a 10 consecutive numbers from any :")
    for _ in range(9):
        num = int(input("Enter a number: "))
        numbers.append(num)
    
    missing_number = find_missing_number(numbers)
    print("The missing consecutive number is:", missing_number)

if __name__ == "__main__":
    main()
