
def search4vowels(word:str) -> set:
    """指定された単語内の母音を返す"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
    
    