
def search4vowels(word:str) -> set:
    """Žw’è‚³‚ê‚½’PŒê“à‚Ì•ê‰¹‚ð•Ô‚·"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
    
    