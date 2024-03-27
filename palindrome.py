
def longest_palindrome_String(s):
    max_length = 0
    start = 0

    
    for i in range(len(s)):
        
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

    return s[start:start + max_length]

string = "ABJHDSSDADSHLUI"
longest_palindrome_sub_string_is = longest_palindrome_String(string)
print("Longest Palindrome Substring:", longest_palindrome_sub_string_is)
