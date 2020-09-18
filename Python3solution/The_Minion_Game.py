def minion_game(string):
    s = string
    vowel = ['A','E','I','O','U']
    Kevin_count = 0
    Stuart_count = 0
    for i in range(len(s)):
        if s[i] in vowel:
            Kevin_count += len(s)-i
        else:
            Stuart_count +=len(s)-i

    if Kevin_count > Stuart_count:
        print('Kevin '+str(Kevin_count))
    elif Stuart_count > Kevin_count:
        print('Stuart '+str(Stuart_count))
    else:
        print('Draw')
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)
