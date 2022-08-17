itertools.permutations(iterable[, r])

This tool returns successive

length permutations of elements in an iterable.

If
is not specified or is None, then

defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
Task

You are given a string
.
Your task is to print all possible permutations of size

of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string
and the integer value

.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the permutations of the string
on separate lines.

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

st = input('')
st = st.split()
k = st[1]
k = int(k)
a = sorted(list(permutations(st[0],k)))
for i in a:
    
    #print(i)
    j = 0
    while j<k:
        print(i[j],end='')
        j+=1
    print()
