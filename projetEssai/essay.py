print(bin(18))
print(hex(18))
H = "78-D6-F0-C2-18-5D"
L = H.split("-")
txt = ""
dd = []
for elt in L:
    txt = txt + '{0:08b}'.format(int(elt,16))
    dd.append(int(elt,16))
print(txt)
print(dd)

