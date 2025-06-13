from typing import List

class Generator:
    def __init__(self):
        pass

    def generate_sentense(self, nouns: List[str]) -> str:
        '''
        TODO
        generate english sentence from given nouns [0 to n]
        return single sentence that have noun position by order
        '''
        return ". ".join(nouns)