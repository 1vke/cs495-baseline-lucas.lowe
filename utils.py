import string

def is_palindrome(word):
    if not isinstance(word, str):
        raise TypeError(f"Must provide a str argument, got '{type(word).__name__}'")

    word_lower = word.lower()

    # remove all punctuation and space chars from a string
    # https://stackoverflow.com/a/266162 - this helped me out
    translator = str.maketrans('', '', string.punctuation + " ")
    clean_text = word_lower.translate(translator)

    # return the result of the equality of clean_text and the reverse of itself (reversed using the [::-1] slice)
    return clean_text == clean_text[::-1]
