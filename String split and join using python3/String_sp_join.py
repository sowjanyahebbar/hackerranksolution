def split_and_join(line):
    # write your code here
    line = line.split(' ')#line is converted to list of strings
    line = '-'.join(line)#We are joining the string using '-'
    return line
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
