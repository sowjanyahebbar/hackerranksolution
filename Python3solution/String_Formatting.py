def print_formatted(number):
    w = len(str(bin(number)).replace('0b',''))
    for i in range(1,number+1):
        d = str(i).rjust(w)                          #rjust is used for line alignment
        o = str(oct(i)[2:].rjust(w))
        h = str(hex(i)[2:].rjust(w).upper())
       
        b = str(bin(i)[2:].rjust(w))
        print(d,o,h,b)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
