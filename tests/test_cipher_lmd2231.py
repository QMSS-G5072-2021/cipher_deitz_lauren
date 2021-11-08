from cipher_lmd2231 import cipher_lmd2231
import pytest

@pytest.mark.parametrize('example,expected',[
    ('OneSingleWord','TsjXnslqjbtwi'),
    ('lowercase','qtBjwhfxj'),
    ('UPPERCASE','ZUUJWHFXJ'),
    ('A sentence with spaces.','F xjsyjshj Bnym xufhjx.')
])
def test_cipher_multiple_values(example, expected):
    actual = cipher_lmd2231.cipher(example,5)
    assert actual == expected
