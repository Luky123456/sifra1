def sifra(text,posun):
    b=""
    for i in range(0,len(text)):
        if text[i] != " ":
            x=ord(text[i])
            y=((((x-97)+posun)%26)+97)
            b+=chr(y)
        else:
            b+=" "
    return b

print(sifra("ahoj jano",1))

#brute-force dešifrovanie a vybrať podľa toho čo sa zdá ok
def desifrovanie(text):
    b=""
    for i in range(1,26):
        for h in range(0,len(text)):
            if text[h] != " ":
                x = ord(text[h])
                y = ((((x - 97) + i) % 26) + 97)
                b += chr(y)
            else:
                b+=" "
        print(b,end="\n")
        b=""

print(desifrovanie(sifra("ahoj jano",5)))