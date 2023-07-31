
def is_palindrome(slovo):
    ishodnoe_slovo = slovo.lower()
    obrabotanoe_slovo = ishodnoe_slovo[::-1]
    if ishodnoe_slovo == obrabotanoe_slovo :
        return True
    else:
        return  False

