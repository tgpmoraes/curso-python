# class Sentence():
#     def __init__(self, sentence):
#         self.sentence = sentence.split(' ')

#     def __iter__(self):
#         return self

#     def __next__(self):
#         try:
#             return self.sentence.pop()
#         except IndexError:
#             raise StopIteration

def sentence(sentence):
    for word in sentence.split():
        yield word


if __name__ == '__main__':
    my_sentence = sentence('This is a test')

    for word in my_sentence:
        print(word)
