import base64


def encrypt_base64():
    text = input("Podaj tekst do zaszyfrowania:")
    encoded_text = base64.b64encode(text.encode())
    print("Zaszyfrowany tekst:", encoded_text.decode())


encrypt_base64()
