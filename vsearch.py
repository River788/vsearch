"""
Practice-Python
"""


def search4vowels(phrase:str) -> set:
    """指定された単語内の母音を返す"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
#PEP8 によると、トップレベル関数では、
#2行の空行を開けることを推奨しています。
def search4letters(phrase:str, letters:str,) -> set:
    """phrase内のlettersの集合を返す。"""
    return set(letters).intersection(set(phrase))
    



