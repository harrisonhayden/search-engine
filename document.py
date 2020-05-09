"""
This file implements the Document class, which
takes in a document, parses it, and extracts different information pertaining
to the words in the document
"""
import re


class Document:
    """
    Class that takes a document from a file and implements all the functions
    to provide information about the file for searching in the search engine
    """
    def __init__(self, doc_file):
        """
        Initializes the Document class, taking a file name as a parameter
        and precomputing: a dictionary containing the frequency of words
        in the document, a list containing all unique words appearing in
        the document, and an integer with the total number of words
        Performs all of this insensitive of casing and punctuation
        """
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
        """
        Returns the path of the file as a string
        """
        return self._path

    def term_frequency(self, term):
        """
        Takes in a string parameter of a word in the document and returns
        the relative frequency of that word in the document, computed in the
        initializer
        Returns 0 if the word is not in the document
        Ignores casing and punctuation
        """
        term = term.lower()
        term = re.sub(r'\W+', '', term)

        if term not in self._frequency:
            return 0
        else:
            return self._frequency[term]

    def get_words(self):
        """
        Returns a list of the unique words in the document
        """
        return self._uniques
