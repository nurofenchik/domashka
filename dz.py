s = input().lower()
print(s)
if s == s[::-1]:
    print('True')
else:
    print('False')