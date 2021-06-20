import sys
sys.path.insert(1, 'Y:\\bin\\')

from ns_crypto.VigenereCipher import VigenereCipher

# 1: Normal Test
print("Prueba Normal")
key = "KING"
inputMsg = "THE SUN AND THE MAN IN THE MOON"
v = VigenereCipher(key)
encodeMsg = v.encode(inputMsg)
msg = v.decode(encodeMsg[0].Value)
status = "OK" if inputMsg == msg[0] else "ERR"
print("Mensaje:\t\t{0}:\nKey:\t\t\t{1}\nVector:\t\t\t{2}\nMensaje Encriptado:\t{3}\nValidación Cipher:\t{4}".format(
    inputMsg, key, v.Vector, encodeMsg[0].Value, status))

# 2: Incomplete Key
print("\n\nPrueba Llave incompleta")
key = "%O"
inputMsg = "BWGWBHQSJBBKNF"
v = VigenereCipher(key)
msg = v.decode(inputMsg)
msgAsString = "\n".join(list(map(lambda x: str(x), msg)))
print("Las posibles respuestas para el mensaje '{0}' son: \n{1}\nLa respuesta con el texto más sensible es '{2}' con llave '{3}'".format(
    inputMsg, msgAsString, msg[9].Value, msg[9].Key))
v = VigenereCipher(msg[9].Key)
encodeMsg = v.encode(msg[9].Value)
print("Validación del Cipher: {0}".format(
      "OK" if encodeMsg[0].Value == inputMsg else "ERR"))

# 3: Mensaje Circular
# Suppose we repeatedly encrypt a certain message with the same password using a Vingenère encryption scheme.
# How many times will we have to encrypt the message SADBOI with the key BAD so that the repeatedly encrypted string will be SADBOI again?
count = 0
inputMsg = "SADBOI"
key = "BAD"
encryptMsg = None
v = VigenereCipher(key)
while inputMsg != encryptMsg:
    if encryptMsg is None:
        encryptMsg = inputMsg
    result = v.encode(encryptMsg)[0]
    encryptMsg = result.Value
    count += 1
    print("I({0}) {1}".format(count, str(result)))
