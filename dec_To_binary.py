'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def dec_To_binary(n):
    binary_num = []
    
    while n > 0:
        binary_num.append(n%2)
        n = n//2
        
    binary_num.reverse()
    
    for digit in binary_num:
        print(digit,end="")

decimal_num = int(input("enter the digits :"))
print("binary form is :",end=" ")
dec_To_binary(decimal_num)
    