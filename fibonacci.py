#Program to display the Fibonacci sequence
nterms = 0

while nterms == 0:
    try:
        nterms = int(input('How many terms?'))
    except:
        print('Please just a positive integer')
#first two terms

n1, n2 = 0, 1
count = 0

#check if the number of terms is valid
if nterms <= 0:
    print('Please enter a positive integer')
#fibonacci sequence
else:
    print('Fibonacci sequence:')
while count < nterms:
        print(n1)
        nth = n1 + n2
        #uptade values
        n1 = n2
        n2 = nth
        count = count + 1

