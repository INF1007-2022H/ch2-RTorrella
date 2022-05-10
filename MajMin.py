print ("Donner une lettre")
x=input('')
if ord(x)>=65 and ord(x)<=90:
    x=ord(x) + 32
    print("Cette lettre en minuscule est " + chr(x))
elif ord(x)>=97 and ord(x)<=122:
    x=ord(x) - 32
    print("Cette lettre en majuscule est " + chr(x))