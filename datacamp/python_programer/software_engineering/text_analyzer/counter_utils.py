from collections import Counter
import matplotlib.pyplot as plt


def plot_counter_most_common(top_items):
    top_items_dict = dict(top_items)
    plt.figure()
    plt.bar(range(len(top_items_dict)),
            list(top_items_dict.values()),
            align='center')
    plt.xticks(range(len(top_items_dict)),
               list(top_items_dict.keys()),
               rotation='vertical')
    plt.tight_layout()
    plt.show()


def sum_counters(counters):
    # Sum the inputted `counters`
    return sum(counters, Counter())


def plot_counter(counter, n_most_common=5):
    # Subset the `n_most_common` items from the input `counter`
    top_items = counter.most_common(n_most_common)
    # Plot `top_items`
    plot_counter_most_common(top_items)


def filter_word_counts(word_counts, first_char):
    """Filter Document.word_counts by the first character of the word

    :param word_counts: the word_counts attribute of a Document class instance
    :param first_char: only keep word counts that start with this character

    >>> # How to filter to only words that start with 'A'
    >>> filter_word_counts(document.word_counts, 'A')
    """
    return Counter({k: v for k,
                    v in word_counts.items() if k[0] == first_char})
