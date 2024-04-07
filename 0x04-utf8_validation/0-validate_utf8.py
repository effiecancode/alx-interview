#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    data: a list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """

    byte_count = 0  # tracks no of bytes to be processed in a UTF-8 character
    for i in data:
        if byte_count == 0:
            # indicating the start of a new UTF-8 character
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_count = 1
            elif i >> 4 == 0b1110:
                byte_count = 2
            elif i >> 3 == 0b11110:
                byte_count = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
