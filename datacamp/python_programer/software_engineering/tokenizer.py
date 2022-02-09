import re


def tokenizer(text):
    """Split text into tokens using a regular expression

    This is a wrapper for re.findall with case ignored.

    :param text: text to be tokenized
    :return: a list of resulting tokens

    >>> tokenize("word word 1.22 can't. cannot")
    ['word', 'word', 'can', 't', 'cannot']
    """
    return re.findall(r'[\@|\#][a-zA-z]+', str(text), flags=re.IGNORECASE)
