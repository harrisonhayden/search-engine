import re


class Document:
    # Class that takes a document from a file and implements all the functions
    # to provide information about the file for searching in the search engine

    def __init__(self, doc_file):
        self._frequency = {}
        self._uniques = []
        self._all_words = []
        self._path = str(doc_file)

        with open(doc_file) as file:

            for line in file:
                for word in line.split():
                    word = word.lower()
                    word = re.sub(r'\W+', '', word)
                    if word in self._frequency:
                        self._frequency[word] += 1
                        self._all_words.append(word)
                    else:
                        self._frequency[word] = 1
                        self._uniques.append(word)
                        self._all_words.append(word)

            self._num_words = (len(self._all_words))

            for word in self._frequency:
                self._frequency[word] = (self._frequency[word])/self._num_words

    def get_path(self):
        return self._path

    def term_frequency(self, term):
        term = term.lower()
        term = re.sub(r'\W+', '', term)

        if term not in self._frequency:
            return 0
        else:
            return self._frequency[term]

    def get_words(self):
        return self._uniques
