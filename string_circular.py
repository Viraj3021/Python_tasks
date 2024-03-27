def rotation_of_String(string1, string2):
    if len(string1) != len(string2):
        return False

    Temp = string1 + string1

    if string2 in Temp:
        return True
    else:
        return False

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if rotation_of_String(string1, string2):
    print(f"{string2} is a rotation of {string1}.")
else:
    print(f"{string2} is not a rotation of {string1}.")
