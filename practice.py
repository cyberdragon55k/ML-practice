string = "A man, a plan, a canal: Panama!"
string = string.replace(" ","")
string = string.replace("'","")
string = string.replace(",","")
string = string.replace(":","")
string = string.replace("!","")
string=string.lower()


if string == string[::-1] :
    print("the string is pallendrome")
else:
    print('the string is not a pallendrome')
