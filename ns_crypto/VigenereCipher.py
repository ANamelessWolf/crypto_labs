from ns_crypto.VigenereCipherResult import VigenereCipherResult

class VigenereCipher:

    EN_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    EN_ALPHABET_CS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ES_ALPHABET = "AÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ"
    ES_ALPHABET_CS = "AÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZaábcdeéfghiíjklmnñoópqrstuúvwxyz"


    def __init__(self, key, alphabet=EN_ALPHABET):
        """Inicializa una instancia del cipher Vigenère

        Args:
            key (string): La llave de encriptación o password
            alphabet (string, optional): El alfabeto que soporta el Cipher. Defaults to EN_ALPHABET.
        """
        #1: Inicialización de variables
        self.Alphabet = alphabet
        self.CipherMatrix = []
        self.Key = key
        self.Vector = None
        self.Message = ""
        alpSize = len(alphabet)
        #2: Se convierte el alfabeto a un arreglo
        words = [char for char in alphabet]
        #3: Se llena la matriz Cipher
        self.__addRow(words)
        for letterIndex in range(1, alpSize):
            last = words[0]
            for i in range(1, alpSize):
                words[i-1] = words[i]
            words[len(words)-1] = last
            self.__addRow(words)

    def __addRow(self, words):
        """Se agrega una fila a la matriz del Cipher

        Args:
            words (list): El alfabeto en un orden especifico como arreglo
        """
        wordsCp = words.copy()
        self.CipherMatrix.append(wordsCp)

    def __generateKeys(self):
        """Se generan las posibles combinaciones de llaves cambiando el caracter wild card '%'

        Returns:
            list: La lista de llaves(passwords) con los que se codificara o decodificará el mensaje
        """
        testKeys = []
        for ch in self.Alphabet:
            key = self.Key.replace("%", ch)
            testKeys.append(key)
        return testKeys

    def __initVector(self, key, msg):
        """Se inicializa el vector con la llave proporcionada. El vector se llenará con
        la llave hasta llegar al tamaño del mensaje.

        Args:
            key (string): La llave o password para generar el vector
            msg (string): El mensaje a tratar

        Returns:
            string: El vector para realizar el proceso de encriptación
        """
        self.Vector = ""
        index = 0
        for ch in msg:
            if ch not in self.Alphabet:
                self.Vector += ch
            else:
                if index == len(key):
                    index = 0
                self.Vector += key[index]
                index += 1
        return self.Vector

    def __decode(self):
        """Realiza la decodificación del mensaje actual. El mensaje esta guardado en la
        propiedad self.Message

        Returns:
            list: La lista de mensajes decodificados
        """
        result = ""
        for index in range(0, len(self.Message)):
            ciphertextCH = self.Message[index]
            if ciphertextCH in self.Alphabet:
                keywordCH = self.Vector[index]
                result += self.getDecodeValue(keywordCH, ciphertextCH)
            else:
                result += ciphertextCH
        return result

    def __encode(self):
        """Realiza la encriptación del mensaje actual. El mensaje esta guardado en la
        propiedad self.Message

        Returns:
            list: La lista de mensajes decodificados
        """
        result = ""
        for index in range(0, len(self.Message)):
            plaintextCH = self.Message[index]
            if plaintextCH in self.Alphabet:
                keywordCH = self.Vector[index]
                result += self.getEncodeValue(keywordCH, plaintextCH)
            else:
                result += plaintextCH
        return result

    def getEncodeValue(self, keywordCH, plainTextCH):
        """Devuelve el caracter encriptado. Busca un caracter asociado a la matriz Cipher, asociando
        un caracter de la llave como fila y un caracter del mensaje como columna

        Args:
            keywordCH (string): El caracter del password
            plainTextCH (string): El caracter del mensaje a encriptar

        Returns:
            string: El caracter encriptado
        """
        rowIndex = self.Alphabet.index(keywordCH)
        colIndex = self.Alphabet.index(plainTextCH)
        return self.CipherMatrix[rowIndex][colIndex]

    def getDecodeValue(self, keywordCH, ciphertextCH):
        """Devuelve el caracter decodificado buscandolo en la matriz Cipher, asociando
        un caracter de la llave como fila y un caracter del mensaje encriptado como columna

        Args:
            keywordCH (string): El caracter del password
            ciphertextCH (string): El caracter del mensaje encriptado

        Returns:
            string: El caracter decodificado
        """        
        rowIndex = self.Alphabet.index(keywordCH)
        matrix = "".join(self.CipherMatrix[rowIndex])
        wordIndex = matrix.index(ciphertextCH)
        return self.Alphabet[wordIndex]

    def encode(self, msg):
        """Realiza la encriptación del mensaje seleccionado

        Args:
            msg (string): El mensaje a encriptar

        Returns:
            list: La Lista de mensajes encriptados
        """
        result = []
        self.Message = msg
        if "%" in self.Key:
            testKeys = self.__generateKeys()
            for key in testKeys:
                self.__initVector(key, msg)
                result.append(VigenereCipherResult(key, self.__encode()))
        else:
            self.__initVector(self.Key, msg)
            result.append(VigenereCipherResult(self.Key, self.__encode()))
        return result

    def decode(self, msg):
        """Realiza la decodificación de un mensaje encriptado

        Args:
            msg (string): El mensaje encriptado

        Returns:
            list: La lista de mensajes decodificados
        """
        result = []
        self.Message = msg
        if "%" in self.Key:
            testKeys = self.__generateKeys()
            for key in testKeys:
                self.__initVector(key, msg)
                result.append(VigenereCipherResult(key, self.__decode()))
        else:
            self.__initVector(self.Key, msg)
            result.append(VigenereCipherResult(self.Key, self.__decode()))
        return result
