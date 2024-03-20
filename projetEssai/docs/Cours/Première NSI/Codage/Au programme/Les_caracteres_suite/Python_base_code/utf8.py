def car_en_utf8(car):
    if ord(car)>= 128:
        txt = (u'{0}'.format(car)).encode('utf-8')
        rep = ""
        for elt in txt:
            rep = rep + hex(elt)[2:] + " "
        return rep[:-1]
    else:
        return hex(ord(car))[2:]

print(car_en_utf8('A') + "en hexadecimal")