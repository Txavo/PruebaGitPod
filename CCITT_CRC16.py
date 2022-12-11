import struct

class ccitt_crc_xmodem:
    def __init__(self, seed):
        self.seed = seed


    def ccitt_crc16(data: bytes) -> int:

        # Inicializamos el CRC con el valor inicial predeterminado
        crc = 0x0000

        # Iteramos sobre cada byte de datos
        for byte in data:
            # Aplicamos una operación XOR en el byte actual y el CRC actual
            crc ^= byte << 8

            # Realizamos un bucle de 8 iteraciones para calcular el CRC
            for _ in range(8):
                # Si el valor más significativo del CRC es 1, entonces aplicamos la
                # fórmula de CCITT para calcular el CRC
                if crc & 0x8000:
                    crc = (crc << 1) ^ self.seed
                # Si el valor más significativo del CRC es 0, entonces solo
                # desplazamos el CRC a la izquierda
                else:
                    crc <<= 1

        # Aplicamos una máscara al CRC final para obtener solo los 16 bits más significativos
        return crc & 0xFFFF

    
CntMessage  = int('0x00', 16)     # 1 byte
Command     = int('0x00', 16)     # 1 byte
OpCodMSB    = int('0x00', 16)     # 1 byte
OpCodLSB    = int('0x04', 16)     # 1 byte

    
a_bytesToSend =  (struct.pack('B', CntMessage)  +
                  struct.pack('B', Command)     +
                  struct.pack('B', OpCodMSB)    +
                  struct.pack('B', OpCodLSB))   

OpCodLSB    = int('0x06', 16)     # 1 byte

b_bytesToSend =  (struct.pack('B', CntMessage)  +
                  struct.pack('B', Command)     +
                  struct.pack('B', OpCodMSB)    +
                  struct.pack('B', OpCodLSB))   


obj_a = ccitt_crc_xmodem(0x1021)
obj_b = ccitt_crc_xmodem(0x1021)

CRC_a_int = obj_a.ccitt_crc16(a_bytesToSend)
CRC_b_int = obj_b.ccitt_crc16(b_bytesToSend)

CRC_a_hex = CRC_a_int.to_bytes(2, 'big').hex() 
CRC_b_hex = CRC_b_int.to_bytes(2, 'big').hex() 

print([CRC_a_hex[x:x+2] for x in range(0, len(CRC_a_hex), 2)])
print([CRC_b_hex[x:x+2] for x in range(0, len(CRC_b_hex), 2)])


# 00 04 (liberar)   CRC 41 84
# 00 06 (accionado) CRC 61 C6