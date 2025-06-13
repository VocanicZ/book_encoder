from typing import List
import pandas as pd
from inflecteur import inflecteur
import spacy
import random

class Noun:
    def __init__(self):
        self._inf = inflecteur()
        self._nlp_en = spacy.load("en_core_web_sm")
        self._nlp_fr = spacy.load("fr_core_news_sm")
        self._inf.load_dict()
        self._nouns = self._get_nouns()
        self._male_nouns = self._get_male_nouns()
        self._female_nouns = self._get_female_nouns()
    
    def _get_nouns(self):
        '''
        get all nouns available from dela-fr-public dictionary
        '''
        df = self._inf.dico_transformer
        # Filter for nouns only
        noun_df = df[df["gram"] == "Nom"]
        return noun_df

    def _get_male_nouns(self):
        '''
        get all male nouns available from dela-fr-public dictionary
        '''
        noun_df = self._nouns
        # Find rows with 'm' in any 'forme'
        mask_male = noun_df["forme"].str.contains(r"\bm\b|[^a-z]m|m[^a-z]", regex=True) | noun_df["forme"].str.contains("m")
        return noun_df[mask_male].index.unique().tolist()

    def _get_female_nouns(self):
        '''
        get all female nouns available from dela-fr-public dictionary
        '''
        noun_df = self._nouns
        # Find rows with 'f' in any 'forme'
        mask_female = noun_df["forme"].str.contains(r"\bf\b|[^a-z]f|f[^a-z]", regex=True) | noun_df["forme"].str.contains("f")
        return noun_df[mask_female].index.unique().tolist()
    
    def get_gender(self, word):
        '''
        return 
        '''
        try:
            df = self._inf.dico_transformer
            if word not in df.index:
                return None
            forms = df.loc[word]
        except KeyError:
            return None

        # Handle both Series (single row) and DataFrame (multiple rows)
        if isinstance(forms, pd.Series):
            if forms["gram"] != "Nom":
                return None
            joined = forms["forme"]
        else:
            noun_forms = forms[forms["gram"] == "Nom"]["forme"]
            if noun_forms.empty:
                return None
            joined = ":".join(noun_forms.values)

        has_f = 'f' in joined
        has_m = 'm' in joined

        if has_f and has_m:
            return "MF"
        elif has_f:
            return "F"
        elif has_m:
            return "M"
        return None
    
    def filter_nouns(self, sentence: str, fr: bool = False) -> List[str]:
        if fr:
            doc = self._nlp_fr(sentence)
        else:
            doc = self._nlp_en(sentence)
        print(f" |__{sentence}")
        nouns = [token.text for token in doc if token.pos_ == "NOUN"]
        print(f" |__{nouns}")
        return nouns
    
    def random_split_nouns(self, nouns: List[str]):
        '''
        TODO
        randomly group nounces together by order
        from 1 to n and apppend to new list[list[str]]
        example. 
        [a,b,c,d] -> [[a], [b, c], [d]] or
        [a,b,c,d] -> [[a, b, c], [d]] or
        [a,b,c,d] -> [[a], [b], [c, d]]
        '''
        return [nouns]