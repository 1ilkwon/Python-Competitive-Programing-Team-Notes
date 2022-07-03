string = list(map(str, input()))
for i in range(0, len(string)):
    if string[i].isupper():
        print(string[i].lower(),end='')
    elif string[i].islower():
        print(string[i].upper(),end='')

"""
1. 소문자를 대문자로 :  upper()
2. 대문자를 소문자로 : lower()
3. 대문자 인지 판별 : isupper()
4. 소문자 인지 판별 : islower()
"""