
def search4vowels(word:str) -> set:
    """�w�肳�ꂽ�P����̕ꉹ��Ԃ�"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
    
    