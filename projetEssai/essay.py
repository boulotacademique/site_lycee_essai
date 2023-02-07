def avoir_le_bac(note):
    if note >= 10:
        return True
    return False

ma_note = int(input("Votre note ? "))
if not(avoir_le_bac(ma_note)):
    print("Dommage ! mais peut-être êtes-vous au rattrapage ?")