
def encrypt_letter(letter, shift):
    if letter.isalpha():
        base=ord('A') if letter.isupper() else ord('a')
        return chr((ord(letter) - base + shift) % 26 + base)
    else:
        raise ValueError("invalid character: {}".format(letter))

def encrypt_message(message, shift):
    vysledek= ""
    for letter in message:
        if not letter.isalpha():
            vysledek += letter
        else:
            vysledek += encrypt_letter(letter,shift)
    return vysledek               


"""print(encrypt_letter("A",3))
print(encrypt_letter("Z",6))
print(encrypt_message("Ahoj jak se mas",4))"""

message = "To claim the hidden 1 million CZK, start by locating the old oak tree near the abandoned railway station. From there, walk exactly 147 steps north until you reach a small stone marked with a red \"X\". Beneath the stone, you will find a metal box containing further instructions. Follow them carefully — only those who pay close attention to every detail will reach the final reward."
#print(encrypt_message(message,3))

def decrypt_letter(letter,shift):
    if letter.isalpha():
        base=ord('A') if letter.isupper() else ord('a')
        return chr((ord(letter) - base - shift) % 26 + base)
    else:
        raise ValueError("invalid character: {}".format(letter))

def decrypt_message(message,shift):
    vysledek= ""
    for letter in message:
        if not letter.isalpha():
            vysledek += letter
        else:
            vysledek += decrypt_letter(letter,shift)
    return vysledek  

encoded_text = """
Kyv grky kf kyv yzuuve 125 fletvj fw xfcu svxzej rk kyv efikyvie xrkv fw kyv fcu tvdvkvip. Giftvvu vrjknriu rcfex kyv tirtbvu jkfev nrcc wfi rggifozdrkvcp 150 dvkvij, lekzc pfl uzjtfmvi r xrkv tfmvivu ze zmp. Svyzeu zk, slizvu yrcw r dvkvi uvvg svevrky kyv kyziu xirmvjkfev fe kyv cvwk, czvj r jvrcvu vemvcfgv. Zejzuv, pfl nzcc wzeu kyv wzerc tclv evvuvu kf lecftb pfli gizqv. Jkrp jyrig — efk vmvipkyzex zj rj zk jvvdj.
"""


"""
for i in range(26):
    print(decrypt_message(encoded_text,i))
    print(i)"""

def encrypt_with_key(text,key):
    result=""
    key_indices=[ord(k.lower()) - ord('a') for k in key]
    key_len=len(key)
    for i,char in enumerate(text):
        if char.isalpha():
            base=ord('A') if char.isupper() else ord('a')
            shift=key_indices[i%key_len]
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

print(encrypt_with_key("ahoj jak se mas", "prezident"))