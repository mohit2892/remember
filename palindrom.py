'''

FIND pelindrom number (DS)
'''
def ispelindrom(s: str) ->bool:
    n = len(s)
    for i in range(n//2):
        if(s[i] != s[i-1-i]):
            break
    return(i == n//2-1)
