"""
Practice-Python
"""


def search4vowels(phrase:str) -> set:
    """�w�肳�ꂽ�P����̕ꉹ��Ԃ�"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
#PEP8 �ɂ��ƁA�g�b�v���x���֐��ł́A
#2�s�̋�s���J���邱�Ƃ𐄏����Ă��܂��B
def search4letters(phrase:str, letters:str,) -> set:
    """phrase����letters�̏W����Ԃ��B"""
    return set(letters).intersection(set(phrase))
    



