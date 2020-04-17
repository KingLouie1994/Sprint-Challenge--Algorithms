'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    total = 0
    if "th" not in word:
        return total
    else:
        total += 1 + count_th(word.replace("th", "lol", 1))
    return total
    
print(count_th(""))        
print(count_th("abcthxyz"))
print(count_th("abcthefthghith"))
print(count_th("thhtthht"))
print(count_th("THtHThth"))

# Source: https://www.tutorialspoint.com/python/string_replace.htm