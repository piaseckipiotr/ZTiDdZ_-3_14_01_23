import base64


def decrypt_base64():
    text = input("Podaj tekst do odszyfrowania:")
    decoded_text = base64.b64decode(text).decode()
    print("Odszyfrowany tekst:", decoded_text)


decrypt_base64()
