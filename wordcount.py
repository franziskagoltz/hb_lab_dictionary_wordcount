# put your code here.
import re


def create_dict(file_name):
    poem_text = open(file_name)

    poem_words = {}

    for line in poem_text:
        line_words = line.split()

        for word in line_words:
            poem_words[word.lower()] = poem_words.get(word, 0) + 1

    for key, value in poem_words.iteritems():
        print key, value

    poem_text.close()
    return poem_words

create_dict('test.txt')

