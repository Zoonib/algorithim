#Level 1 Part 1 --- updated

def bin_go(n:int):
    for i in range(1, n+1):
        if i %3 == 0 and i % 7 == 0:
            print("bingo")
        elif i % 7 == 0:
          print("go")  
        elif i % 3 == 0:
            print("bin")
        else:
            print(i)
# bin_go(100)
      
#Level 1 Part 2 --- updated
#Compute the sum of digits in all numbers from 1 to n
def sum_of_number(number: int):
    result = 0
    for i in range(1, number+1):
        result += i #result = result + i
        print(result)

#1, 2, 3, 4, 5
sum_of_number(5)

#Level 2 Part 1
#find Max number

def find_max(a: int, b: int, c: int):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c

print(find_max (124, 21, 32))


# Level 2 part 2
#Leap Year

def leap_year(year: int):
    if year % 4:
        if year % 100:
            if year % 400:
                print(f"{year}is a leap year")
            else:
                print(f"{year}is not a leap year")
        else:
             print(f"{year}is a leap year")
    else:
        print(f"{year}i s not a leap year")
        
leap_year(1992) # true
leap_year(2000) #true
leap_year(2100) #false
leap_year(2071) #false
                
                
    #Level 3 Fibonocci sequence
    
def generate_fibonacci_sequence(n: int):
# Initialize the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]
    # Use a for loop to generate the remaining Fibonacci numbers after the first two
    for i in range(2, n):
        new_number = fib_sequence [-1] + fib_sequence [-2]
        fib_sequence.append(new_number)
# Calculate the next Fibonacci number using the formula fib_sequence[-1] + fib_sequence[-2]
            
        
# Append the new Fibonacci number to the list using the append() function
       

    return fib_sequence

    
print(generate_fibonacci_sequence(10))