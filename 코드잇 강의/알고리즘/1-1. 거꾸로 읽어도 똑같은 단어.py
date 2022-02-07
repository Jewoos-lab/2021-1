#답지보고 품.. 어렵다

# 쉬운 풀이
# list_word = list(word)
# reversed_word = ''.join(reversed(list_word))
# return reversed_word == word

def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] == word[-i-1]:
            continue
        else:
            return False
    return True


print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))