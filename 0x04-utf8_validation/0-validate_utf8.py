#!/usr/bin/python3

"""
UTF-8 Validation

a method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):

    """

    A method that determines if a given data set
    represents a valid UTF-8 encoding or not

    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False

    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    """
    remaining_bytes = 0
    byte_mask_1 = 1 << 7  # 10000000
    byte_mask_2 = 1 << 6  # 01000000

    for num in data:
        current_byte = num & 0xFF

        if remaining_bytes > 0:
            # Not in form '10xxxxxx'
            if not (current_byte & byte_mask_1 and not (current_byte & byte_mask_2)):
                return False
            remaining_bytes -= 1
        else:
            # 1-byte character (0xxxxxxx)
            if (current_byte & byte_mask_1) == 0:
                continue
            # Invalid scenario, as it cannot start with 10xxxxxx
            elif (current_byte & (byte_mask_1 | byte_mask_2)) == byte_mask_1:
                return False
            # 2-byte character (110xxxxx)
            elif (current_byte & (byte_mask_1 | byte_mask_2 | (1 << 5))) == (byte_mask_1 | byte_mask_2):
                remaining_bytes = 1
            # 3-byte character (1110xxxx)
            elif (current_byte & (byte_mask_1 | byte_mask_2 | (1 << 5) | (1 << 4))
                  ) == (byte_mask_1 | byte_mask_2 | (1 << 5)):
                remaining_bytes = 2
            # 4-byte character (11110xxx)
            elif (current_byte & (byte_mask_1 | byte_mask_2 | (1 << 5) | (1 << 4) | (1 << 3))
                  ) == (byte_mask_1 | byte_mask_2 | (1 << 5) | (1 << 4)):
                remaining_bytes = 3
            else:
                return False
    return remaining_bytes == 0

