import pandas as pd
from textblob import TextBlob

class TamazightBridge:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.tifinagh_map = {
            'a': 'ⴰ', 'b': 'ⴱ', 'g': 'ⴳ', 'd': 'ⴷ', 'e': 'ⴻ', 'f': 'ⴼ', 
            'k': 'ⴽ', 'h': 'ⵀ', 'i': 'ⵉ', 'j': 'ⵊ', 'l': 'ⵍ', 'm': 'ⵎ', 
            'n': 'ⵏ', 'u': 'ⵓ', 'r': 'ⵔ', 's': 'ⵙ', 't': 'ⵜ', 'q': 'ⵇ',
            'w': 'ⵡ', 'x': 'ⵅ', 'y': 'ⵢ', 'z': 'ⵣ', ' ': ' '
        }

    def to_tifinagh(self, text):
        return "".join([self.tifinagh_map.get(c.lower(), c) for c in text])

    def detect_script(self, text):
        tifinagh_chars = sum(1 for c in text if '\u2D30' <= c <= '\u2D7F')
        arabic_chars = sum(1 for c in text if '\u0600' <= c <= '\u06FF')
        if tifinagh_chars > 0: return "Tifinagh"
        if arabic_chars > 0: return "Arabic"
        return "Latin"

    def translate_simple(self, word, target_lang='English'):
        res = self.df[self.df['Español'].str.contains(word, case=False, na=False)]
        return res[['Tamazight', 'Dialecto', target_lang]].to_dict('records')

print("✅ Archivo 'tamazight_bridge.py' creado con éxito.")
