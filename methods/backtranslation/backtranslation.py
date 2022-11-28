"""Utilities for performing backtranslation."""
from translate import Translator

from preprocessing import split_text_on_char_limit

ENGLISH_TO_SPANISH_TRANSLATOR = Translator(from_lang="en", to_lang="es")
SPANISH_TO_ENGLISH_TRANSLATOR = Translator(from_lang="es", to_lang="en")

EXAMPLE_TEXT = """
    Starting in the late 1950s, American computer scientist Paul Baran
    developed the concept Distributed Adaptive Message Block Switching with
    the goal to provide a fault-tolerant, efficient routing method for
    telecommunication messages as part of a research program at the RAND
    Corporation, funded by the US Department of Defense. This concept
    contrasted and contradicted the theretofore established principles of
    pre-allocation of network bandwidth, largely fortified by the development
    of telecommunications in the Bell System. The new concept found little
    resonance among network implementers until the independent work of
    Donald Davies at the National Physical Laboratory (United Kingdom)
    (NPL) in the late 1960s. Davies is credited with coining the modern
    name packet switching and inspiring numerous packet switching networks
    in Europe in the decade following, including the incorporation of the
    concept in the early ARPANET in the United States.
"""

CHAR_LIMIT = 500

def do_backtranslation(text: str) -> str:
    texts_to_translate = split_text_on_char_limit(
        text=text, char_limit=CHAR_LIMIT
    )
    spanish_translations = [
        ENGLISH_TO_SPANISH_TRANSLATOR.translate(text)
        for text in texts_to_translate
    ]
    spanish_translations_joined = " ".join(spanish_translations)
    spanish_translations_split = split_text_on_char_limit(
        text=spanish_translations_joined, char_limit=CHAR_LIMIT
    )
    english_backtranslation = [
        SPANISH_TO_ENGLISH_TRANSLATOR.translate(text)
        for text in spanish_translations_split
    ]
    english_backtranslation_joined = " ".join(english_backtranslation)
    return english_backtranslation_joined

if __name__ == '__main__':
    english_backtranslation = do_backtranslation(EXAMPLE_TEXT)
    breakpoint()
