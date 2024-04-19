'''print(range(1,5))
print(list(range(1,5)))
print(list(range(1,20,3)))
print(list(range(5,1)))

for a in range(0,6):
    print(a)

'''
'''# Odd number printing
n = int(input("Enter the number: "))
for i in range(1,n,2):
    print(i)
    '''

'''# First n odd numbers
n = int(input("Enter the number: "))
for i in range(1,2*n):
    if(i%2==1):
        print(i, end=" ")

        '''

# AP
'''a = int(input("Enter the first number: "))
d = int(input("Enter the coomon difference: "))
n = int(input("Enter the number of terms: "))
for i in range(a, (a+(n-1)*d)+1, d):
    print(i, end=" ")
    '''

'''# GP
def print_gp():
    a = int(input("Enter the first term: "))
    r = int(input("Enter the common ratio: "))
    n = int(input("Enter the number of terms: "))
    curr_term = 1
    for i in range(1,n+1,1):
        curr_term = a*(r**(i-1))
        print(curr_term)

print_gp()

'''



'''# HP
def harmonic_progression():
    a = int(input("Enter the first term: "))
    d = int(input("Enter the common difference: "))
    n = int(input("Enter the number of terms: "))
    for i in range(1,n+1,1):
        curr_term = 1/(a+(i-1)*d)
        print(curr_term)

harmonic_progression()
        
'''


'''# Table
def printing_table():
    table_no = int(input("Enter the number: "))
    for i in range(0,20):
        print(table_no, "*", i+1, "->", table_no*(i+1))

printing_table()

'''

'''# sum of digit of a number
num = int(input("Enter the number: "))
sum = 0
while num>0:
    sum+=(num%10)
    num//=10

print(sum)
'''

'''# Given a number, print its divisor
def print_divisor():
    num = int(input("Enter the number: "))
    for i in range(1,num):
        if(num%i==0):
            print(i)

print_divisor()
'''


'''# five stars in five line
for i in range(0,5):
    for j in range(0,5):
        print("*", end="")
    print("\n")    
'''

'''# printing digits with respective line
num = int(input("Enter the number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j, end="")
    print("\n")
    '''

# upper triangular and lower triangular together

