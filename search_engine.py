"""
Harrison Hayden Section AD - this file acts as a search engine, taking in
a file directory and helping compute the relevance of a document in the
directory to a given term using TF-IDF
"""
import math
import os
import re
from document import Document


class SearchEngine:
    """
    Class that implements TFIDF to act as a search engine for a collection of
    files
    """
    def __init__(self, dir_name):
        """
        Initializes the SearchEngine classs, taking a directory name as a
        parameter and precomputes an inverse index in a dictionary as well
        as the total number of documents in the directory and a dictonary
        mapping a word to its number of document occurences
        """
        self._dir = dir_name + '/'
        self._docs = {}
        self._inv_idx = {}
        self._num_docs_with_word = {}
        terms = []

        for file_name in os.listdir(dir_name):
            directory = dir_name + '/' + file_name
            self._docs[file_name] = Document(directory)

        self._num_docs = len(self._docs)

        for doc in self._docs:
            terms = self._docs[doc].get_words()
            for word in terms:
                if word in self._inv_idx.keys():
                    self._inv_idx[word].append(doc)
                    self._num_docs_with_word[word] += 1
                else:
                    self._inv_idx[word] = [doc]
                    self._num_docs_with_word[word] = 1

    def _calculate_idf(self, term):
        """
        Takes a string parameter of a word and calculates its idf across
        all documents in the directory
        Returns 0 if the word is not in any document
        Ignores casing and punctuation
        """
        term = term.lower()
        term = re.sub(r'\W+', '', term)

        if term not in self._inv_idx:
            return 0
        else:
            num = self._num_docs_with_word[term]
            return math.log(self._num_docs/num)

    def search(self, term):
        """
        Takes a string parameter of any number of words, calculates the
        TFIDF of each word and the search as a whole, and returns a list of
        relevant documents sorted from most to least relevant
        """
        terms = term.split()
        term = term.lower()
        term = re.sub(r'\W+', '', term)
        list = []

        for doc in self._docs:
            total = 0
            for term in terms:
                doc_full = Document(self._dir + doc)
                tf = doc_full.term_frequency(term)
                dir = SearchEngine(self._dir)
                idf = dir._calculate_idf(term)
                tf_idf = tf * idf
                total += tf_idf
            if total > 0:
                tuple = str(self._dir + doc), total
                list.append(tuple)
        sorted_list = sorted(list, key=lambda x: x[1], reverse=True)

        return [i[0] for i in sorted_list]
