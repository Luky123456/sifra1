def zakod(kod,veta):
    vetan = ""
    z=0
    for o in range(0, len(veta)):
        for i in kod:
            if z> len(veta)-1:
                z = z - len(veta)
                y = ord(veta[z])
                x = ord(i)
                vetan += chr(((((x + y) - 97) % 26) + 97))
            else:
                y = ord(veta[z])
                z += 1
                x = ord(i)
                vetan += chr(((((x+y) - 97) % 26) + 97))
        return vetan

print(zakod("ahojte","vydla"))
print(zakod("aabaabaab","aabaz"))






