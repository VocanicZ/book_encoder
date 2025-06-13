import random
import textwrap
from typing import List
import time

from .utils.generator import Generator
from .utils.noun import Noun
from .utils.translate import Translate

class BookEncoder:
    def __init__(self):
        print("Setting up..")
        start = time.time()

        self._tsl = Translate()
        self._noun = Noun()
        self._gen = Generator()

        print(f"Done! {time.time()-start}")
    
    def encode_to_france(self, message: str) -> str:
        return self.encode(message, fr_str=True)
        
    def encode(self, message: str, fr_str: bool = False) -> str:
        binary = ''.join(format(ord(c), '08b') for c in message)
        print(f"Binary representation of message: {binary}, len {len(binary)}")
        fr_nouns = []

        for bit in binary:
            if bit == '1':
                fr_noun = random.choice(self._noun._male_nouns)
            else:
                fr_noun = random.choice(self._noun._female_nouns)
            fr_nouns.append(fr_noun)

        print(f"fr nouns len {len(fr_nouns)}")
        print(fr_nouns)
        nouns = []
        for fr_noun in fr_nouns:
            noun = self._tsl.translate_to_english(fr_noun)
            nouns.append(noun)
        
        encrypted_sentences = []
        nouns_list = self._noun.random_split_nouns(nouns)
        for n in nouns_list:
            sentence = self._gen.generate_sentense(n)
            if fr_str:
                sentence = self._tsl.translate_to_french(sentence)
            encrypted_sentences.append(sentence)
        print(f"encripted sentenses len {len(encrypted_sentences)}")
        return ". ".join(encrypted_sentences)
    
    def decode_from_france(self, sentences: List[str]) -> str:
        return self.decode(sentences, fr_str=True)

    def decode(self, message: str, fr_str: bool = False) -> str:
        binary = ""

        sentences = message.split(". ")
        print(f"sentensed len {len(sentences)}")

        nouns = []
        
        for sentence in sentences:
            filter_nouns = self._noun.filter_nouns(sentence, fr_str)
            if not fr_str:
                tmp = []
                for noun in filter_nouns:
                    tmp.append(self._tsl.translate_to_french(noun))
                filter_nouns = tmp
                tmp = None
            nouns.extend(filter_nouns)
        
        print(f"nouns len {len(nouns)}")
        print(nouns)
        for noun in nouns:
            gender = self._noun.get_gender(noun)
            if gender == "M":
                binary += "1"
            elif gender == "F":
                binary += "0"
        
        print(f"Binary representation of encoded sentences: {binary}, len {len(binary)}")
        chars = textwrap.wrap(binary, 8)
        return ''.join(chr(int(c, 2)) for c in chars)
