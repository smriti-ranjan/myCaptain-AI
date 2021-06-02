"""The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …….. In mathematical terms,
the sequence Fn of Fibonacci numbers is defined by the recurrence relation."""

#fibonacci series: fn = fn-1 + fn-2 with f0=0 & f1=1

n = int(input("Enter the number of terms in the series: "))

f0 = 0
f1 = 1
count=0

if n<=0:
    print("Invalid Input!")
elif n==1:
    print("Fibonacci Series: ")
    print(f0)
else:
    print("Fibonacci Series: ")
    while count<n:
        print(f0)
        fn = f0 + f1
        f0 = f1
        f1 = fn
        count+=1
            
