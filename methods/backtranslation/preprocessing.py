"""Preprocess inputs before passing into backtranslation API."""
from typing import List, Literal, Optional

LANGUAGES_TO_ISO = {
    "spanish": "es",
    "french": "fr",
    "german": "de"
}

def split_text_on_char_limit(
    text: str, char_limit: int, delimiters: Optional[List[str]] = [',', '.']
) -> List[str]:
    """Splits text into chunks based on char limits.
    
    Splits on the last instance of the the delimiters. Assumes that within
    the previous `char_limit` chars, there's at least one of the delimiters.
    """
    if len(text) < char_limit:
        return [text]

    output_lst = []

    start_idx_current_substring = 0
    last_valid_delimiter_idx = -1
    current_string_length = 0

    for idx in range(len(text)):
        if text[idx] in delimiters:
            last_valid_delimiter_idx = idx
        if current_string_length < char_limit:
            current_string_length += 1
        else:
            # split on the last valid instance of the delimiter
            # (excluding the delimiter)
            substr = text[start_idx_current_substring:last_valid_delimiter_idx]
            
            # add to list
            output_lst.append(substr)
            
            # update start_idx_current_substring (starting with the last
            # delimiter)
            start_idx_current_substring = last_valid_delimiter_idx
            
            # reset string length
            current_string_length = 0

    return output_lst
