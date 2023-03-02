def charger_message(fichiermessage):
    with open(fichiermessage, 'r') as f:
        content = f.read()
    return content

def charger_crypt(fichiercrypt):
    cryptmess = open(fichiercrypt,"w")
    return cryptmess


def cesarcryptage(text):
    crypt = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                crypt += chr((ord(char) - 65 + 3) % 26 + 65)
            else:
                crypt += chr((ord(char) - 97 + 3) % 26 + 97)
        else:
            crypt += char 
    with open("crypt.txt", "w") as f:
        f.write(crypt)
    return crypt


def cesardecryptage(crypt):
    plain = ''
    for char in crypt:
        if char.isalpha():
            if char.isupper():
                plain += chr((ord(char) - 68) % 26 + 65)
            else:
                plain += chr((ord(char) - 100) % 26 + 97)
        else:
            plain += char 
    return plain

def menu():
    print("1. Crypter un message")
    print("2. Décrypter un message")
    choix = input("Entrez votre choix (1 ou 2): ")
    if choix == "1":
        fichiermessage = 'message.txt'
        fichiercrypt = 'crypt.txt'
        text = charger_message(fichiermessage)
        crypt = charger_crypt(fichiercrypt)
        cryptage = cesarcryptage(text)
        print("Message crypté : ")
        print(cryptage)
    elif choix == "2":
        fichiercrypt = 'crypt.txt'
        crypt = charger_message(fichiercrypt)
        decryptagetext = cesardecryptage(crypt)
        print("Message décrypté : ")
        print(decryptagetext)
    else:
        print("Choix invalide, veuillez entrer 1 ou 2.")


menu()