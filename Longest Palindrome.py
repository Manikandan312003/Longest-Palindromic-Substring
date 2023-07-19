def longestPalindrome(string):
    longestLength,longestString=0,''
    for i in range(len(string)+1):
        for j in range(i):
            reverse=string[j:i]
            if reverse==reverse[::-1] and longestLength<(i-j):
                longestLength=i-j
                longestString=reverse

    return longestString
print(longestPalindrome("abbcbb"))