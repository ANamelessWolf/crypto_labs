class VigenereCipherResult:

    def __init__(self, key, value):
        """Inicializa una instancia de un resultado del Cipher, asocia un password a un resultado
        encriptado

        Args:
            key (string): La llave o password
            value (string): El mensaje asociado a la operación
        """
        self.__Key = key
        self.__Value = value

    @property
    def Key(self):
        """Define la llave o password que usará el Cipher en sus operaciones

        Returns:
            string: La llave o password del Cipher
        """
        return self.__Key

    @property
    def Value(self):
        """El resultado de la operación del Cipher

        Returns:
            string: El resultado de la operación
        """
        return self.__Value

    def __str__(self):
        """Imprime el resultado del Cipher asociando la llave que se uso para la operación

        Returns:
            string: El resultado del Cipher en formato Llave Valor
        """
        return "Password: {0} Result: {1}".format(self.__Key, self.__Value)
