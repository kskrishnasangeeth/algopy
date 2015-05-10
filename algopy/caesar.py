"""Caesar Cipher is one of the most simplest and widely used encryption
technique.  It is a type of substitution cipher in which each letter in 
the plaintext is replaced by a letter some fixed number of positions 
down the alphabet.

Example:

Plain:    ABCDEFGHIJKLMNOPQRSTUVWXYZ

Key used: 3

Cipher:   DEFGHIJKLMNOPQRSTUVWXYZABC

"""

__author__ = 'kskrishnasangeeth'

import string


def __cipher_helper(message, key):
    """Function where the encryption/decryption logic gets executed.

    Args:
        message (str): Message that is supplied for encryption/decryption.
        key (int): Key used for encryption/decryption.

    Returns:
        message (str): Message in lowercase.

    """

    cipher_text = ""
    for each_char in message.lower():
        char_pos = string.ascii_lowercase.find(each_char)
        if char_pos == -1:
            cipher_text += each_char
            continue
        else:
            char_pos = (char_pos + key) % 26
            cipher_text += string.ascii_lowercase[char_pos]
    return cipher_text


def encrypt(message, key):
    """Returns encrypted message.

    The message string  that is passed as argument gets
    encrypted using the key supplied.

    Args:
        message (str): The message to be encrypted.
        key (int): The key based on which encryption is performed.

    Returns:
        str: the encrypted message.

    """
    __check_exceptions(key)
    encrypt_text = __cipher_helper(message, key)
    return encrypt_text


def decrypt(message, key):
    """Returns  decrypted message.

    The encoded message string that is passed as argument gets
    decrypted using the key provided.

    Args:
        message (str): The  message to be decrypted.
        key (int): The key based on which decryption
                   is performed.

    Returns:
        str:  The message which was decrypted.

    """
    __check_exceptions(key)
    decrypt_text = __cipher_helper(message, -key)
    return decrypt_text


def __check_exceptions(key):
    """Function to check and raise exception for wrong key.

    Args:
        key (str): The key for which exceptions are checked
                    against.

    """
    if key <= 0 or key >= 27:
        raise ValueError("Key value should be between 0 and 26. Got Key as", key)