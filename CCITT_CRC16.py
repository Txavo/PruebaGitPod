# def ccitt_crc16(data: bytes) -> int:
def ccitt_crc16(data: bytes):
    # Inicializamos el CRC con el valor inicial predeterminado
    crc = 0xFFFF

    # Iteramos sobre cada byte de datos
    for byte in data:
        # Aplicamos una operación XOR en el byte actual y el CRC actual
        crc ^= byte << 8

        # Realizamos un bucle de 8 iteraciones para calcular el CRC
        for _ in range(8):
            # Si el valor más significativo del CRC es 1, entonces aplicamos la
            # fórmula de CCITT para calcular el CRC
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            # Si el valor más significativo del CRC es 0, entonces solo
            # desplazamos el CRC a la izquierda
            else:
                crc <<= 1

    # Aplicamos una máscara al CRC final para obtener solo los 16 bits más significativos
    return crc & 0xFFFF


bytes_CRC = 

print(ccitt_crc16(bytes_CRC))