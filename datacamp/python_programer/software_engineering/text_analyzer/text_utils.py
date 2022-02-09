import re
from collections import Counter


def tokenize(text):
    """Split text into tokens using a regular expression

    This is a wrapper for re.findall with case ignored.

    :param text: text to be tokenized
    :return: a list of resulting tokens

    >>> tokenize("word word 1.22 can't. cannot")
    ['word', 'word', 'can', 't', 'cannot']
    """
    return re.findall(r'@?#?[a-zA-z]+', text, flags=re.IGNORECASE)


def filter_word_counts(word_counts, first_char):
    """Filter Document.word_counts by the first character of the word

    :param word_counts: the word_counts attribute of a Document class instance
    :param first_char: only keep word counts that start with this character

    >>> # How to filter to only words that start with '@'
    >>> from text_analyzer import Document
    >>> document = Document('@DataCamp has great courses!')
    >>> filter_word_counts(document.word_counts, '@')
    Counter({'@DataCamp': 1})
    """
    return Counter({k: v for k, v in word_counts.items() if k[0] == first_char})


def filter_lines(text, first_chars):
    """Filter lines by beginning characters (case sensitive)

    :param text:  multi-line text to filter
    :param first_chars: required characters for line to start with to be returned
    :return: text with only lines starting with first_chars included

    >>> text = 'humpty dumpty\\nsat on a wall\\nhumpty dumpty\\nhad a great fall'
    >>> filter_lines(text, 'h')
    'humpty dumpty\\nhumpty dumpty\\nhad a great fall'

    >>> filter_lines(text, 'humpty')
    'humpty dumpty\\nhumpty dumpty'
    """
    n_chars = len(first_chars)
    lines = text.split('\\n')

    filtered_lines = [l for l in lines if l[:n_chars] == first_chars]

    return '\\n'.join(filtered_lines)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
