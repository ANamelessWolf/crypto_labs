import numpy as np
import os
from ns_crypto.common.ERROR_MSG import ERROR_MSG
from PIL import Image

"""Define la clase que permite encriptar un mensaje en una imagen usando
el metodo de esteganografía LSB
"""


class ImageSteganography:

    RED = 0
    GREEN = 1
    BLUE = 2
    RGB = [RED, GREEN, BLUE]
    HIDDEN_SEQ = "N@m3l3ss!"
    
    
    def __init__(self, src):
        if not os.path.exists(src):
            raise Exception(ERROR_MSG.ERR_IMG_MISS)
        print("Leyendo imagen {0}...".format(src))
        img = Image.open(src, 'r')
        if img.format != "PNG":
            raise Exception(ERROR_MSG.ERR_BAD_FORMAT)
        self.ImageSrc = src
        self.Data = np.array(list(img.getdata()))
        self.Width, self.Height = img.size
        self.Mode = img.mode
        self.NumOfPixels = self.Data.size/3 if img.mode == 'RGB' else self.Data.size/4
        self.NumOfPixels = int(self.NumOfPixels)

    def to_binary(self, msg):
        # Cada posición del mensaje es transformada a unicode y luego a binario de 8 digitos
        data = map(lambda ch: "{0:08b}".format(ord(ch)), msg)
        data = list(data)
        return "".join(data)

    def add_bit_to_LSB(self, imgColorIndex, ch):
        # Se cambia el LSB por el bit del mensaje(ch)
        bColor = bin(imgColorIndex)[2:9]+ch
        return int(bColor, 2)

    def get_LSB(self, imgColorIndex):
        # Se cambia el LSB por el bit del mensaje(ch)
        ch = bin(imgColorIndex)[2:][-1]
        return ch

    def check_message(self, hidden_message, message, chunk):
        # 1: Cuando el chunk es de 8 bits se procesa
        if len(chunk) == 8:
            # 2: Se obtiene el ch del grupo de bits
            message += chr(int(chunk, 2))
            chunk = ""
            # 3: Se busca primero la seq clave que identifica el mensaje
            if ImageSteganography.HIDDEN_SEQ in message and len(hidden_message) == 0:
                hidden_message += ImageSteganography.HIDDEN_SEQ
                message = ""
            elif len(hidden_message) > 0:
                hidden_message += message[-1]
        return message, chunk, hidden_message

    def messageIsDecoded(self, hidden_message):
        msgArray = hidden_message.split(ImageSteganography.HIDDEN_SEQ)
        return len(msgArray) < 3

    def reshape(self, dest):
        imgModeSize = 3 if self.Mode == 'RGB' else 4
        self.Data = self.Data.reshape(self.Height, self.Width, imgModeSize)
        wrapData = self.Data.astype('uint8')
        enc_img = Image.fromarray(wrapData, self.Mode)
        enc_img.save(dest)

    def get_dest(self):
        dest = os.path.basename(self.ImageSrc)
        directory = os.path.dirname(self.ImageSrc)
        file = dest.split('.')
        dest = os.path.join(
            directory, "{0}-encode.{1}".format(file[0], file[1]))
        return dest

    def encode(self, msg):
        dest = self.get_dest()
        msg = "{}{}{}".format(ImageSteganography.HIDDEN_SEQ,
                              msg, ImageSteganography.HIDDEN_SEQ)
        print("Codificando...")
        bMsg = self.to_binary(msg)
        # 1: Se verifica que el mensaje quepa en la imagen
        if len(bMsg) > self.NumOfPixels:
            raise Exception(ERROR_MSG.ERR_IMG_TO_SMALL)
        # 2: Se itera la imagen y se cambia el LSB con el bit del mensaje
        msgIndex = 0
        imgIndex = 0
        while msgIndex < len(bMsg):
            for cIndex in ImageSteganography.RGB:
                if msgIndex < len(bMsg):
                    self.Data[imgIndex][cIndex] = self.add_bit_to_LSB(
                        self.Data[imgIndex][cIndex], bMsg[msgIndex])
                msgIndex += 1
            imgIndex += 1
        # 3: Se actualiza la imagen y se guarda en la ruta destino
        self.reshape(dest)
        print("Imagen Codificada: {0}".format(dest))

    def decode(self):
        print("Decodificando...")
        hidden_message = ""
        message = ""
        chunk = ""
        pixel = 0
        # 1: Se revisa todos los pixeles de la imagen mientras no se decodifique el mensaje
        while pixel < self.NumOfPixels and self.messageIsDecoded(hidden_message):
            for cIndex in ImageSteganography.RGB:
                # 2: Se obtienen los bits(LSB) de cada pixel y se concatenan en un chunk
                chunk += self.get_LSB(self.Data[pixel][cIndex])
                message, chunk, hidden_message = self.check_message(
                    hidden_message, message, chunk)
            message, chunk, hidden_message = self.check_message(
                hidden_message, message, chunk)
            pixel += 1
        # 2: Validación del proceso de salida
        hMsg = hidden_message.split(ImageSteganography.HIDDEN_SEQ)
        if len(hMsg) == 3:
            msg = hidden_message.split(ImageSteganography.HIDDEN_SEQ)[1]
            return msg
        else:
            raise Exception(ERROR_MSG.ERR_DECODING)
