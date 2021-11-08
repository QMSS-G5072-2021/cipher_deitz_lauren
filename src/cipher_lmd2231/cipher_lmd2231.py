def cipher(text, shift, encrypt=True):
    """
    Encrypts and decrypts words written using a Caesar cipher, which replaces a letter with
    another letter a given number of places away in the alphabet.

    Parameters
    ----------
    text : String
        The String that should be processed in the function
    shift : Integer
        The number of alphabetic positions away the individual letters of the String should be
        shifted. Can be positive or negative.
    encrypt : Boolean, default True
        Indicates whether the function should return the text encrypted or decrypted.

    Returns
    -------
    String
      The encrypted or decrypted version of the text input.

    Examples
    --------
    >>> from cipher_lmd2231 import cipher
    >>> cipher(text='OneSingleWord', shift=5, encrypt=True)
    TsjXnslqjbtwi

    Each character in `OneSingleWord` is shifted 5 places ahead.

    >>> cipher(text='TsjXnslqjbtwi', shift=-5, encrypt=True)
    OneSingleWord

    Each character in `TsjXnslqjbtwi` is shifted 5 places back.

    >>> cipher(text='TsjXnslqjbtwi', shift=5, encrypt=False)
    OneSingleWord

    Each character in `TsjXnslqjbtwi` is shifted 5 places back due to the encrypt
    argument.
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
