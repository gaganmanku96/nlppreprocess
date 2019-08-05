to_replace = {'don\'t': 'do not', 'dont': 'do not',
              'doesn\'t': 'does not', 'doesnt': 'does not',
              'didn\'t': 'did not', 'didnt': 'did not',
              'shouldn\'t': 'should not', 'shouldnt': 'should not',
              'haven\'t': 'have not', 'hvn\'t': 'have not',
              'havent': 'have not', 'hadn\'t': 'had not',
              'hadnt': 'had not', 'cannt': 'can not',
              'cann\'t': 'can not', 'couldn\'t': 'could not',
              'couldnt': 'could not', 'nt': 'not'}

stopwords = ['i', 'me', 'mine', 'he', 'she', 'it', 'a', 'an', 'the',
             'above', 'below', 'while', 'as', 'until', 'of', 'at',
             'down', 'if', 'to', 'or', 'was', 'were', 'itself', 'for',
             'other', 'both', 'any', 'all', 'between', 'do', 'does',
             'did', 'on', 'own', 'who', 'whom', 'this', 'that', 'has',
             'have', 'here', 'some', 'why', 'same',
             'so', 'is', 'be']

import re

from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer

class NLP():
    def __init__(self, remove_stopwords=True, replace_words=True,
                 remove_numbers=True, remove_html_tags=True,
                 remove_punctuations=True, lemmatize=False,
                 lemmatize_method='wordnet'):
        """
        This package contains functions that can help during the
        preprocessing of text data.
        :param remove_stopwords: boolean
            default value = True
        :param replace_words: boolean
            default value = True
        """
        if (type(remove_stopwords) != bool or
            type(replace_words) != bool or
            type(remove_numbers) != bool or
            type(remove_html_tags) != bool or
            type(remove_punctuations) != bool or
            type(lemmatize) != bool):
            raise Exception("Error - expecting a boolean parameter")
        if lemmatize_method not in ['wordnet', 'snowball']:
            raise Exception("Error - lemmatizer method not supported")
        self.doc = None
        self.lemmatizer = None
        self.remove_stopwords = remove_stopwords
        self.replace_words = replace_words
        self.remove_numbers = remove_numbers
        self.remove_html_tags = remove_html_tags
        self.remove_punctations = remove_punctuations
        self.lemmatize_method = lemmatize_method
        self.lemmatize = lemmatize
        self.stopword_list = set(stopwords)
        self.replacement_list = to_replace
        if self.lemmatize_method == 'wordnet':
            self.lemmatizer = WordNetLemmatizer()
        if self.lemmatize_method == 'snowball':
            self.lemmatizer = SnowballStemmer('english')
    

    def remove_stopwords_fun(self):
        """
        This function removes stopwords from doc.
        It works by tokenizing the doc and then
        checking if the word is present in stopwords
        """
        tokens = str(self.doc).split()
        cleaned_tokens = [token for token in tokens
                          if token.lower() not in self.stopword_list]
        self.doc = ' '.join(cleaned_tokens)

    def replace_words_fun(self):
        """
        This function replaces words that are --
        by checking a word if a word is present in a dictionary
        if the word is present in dictionary then it is replaced
        with its value from dictionary
        """

        cleaned_doc = []
        for word in str(self.doc).split():
            if word.lower() in self.replacement_list.keys():
                cleaned_doc.append(self.replacement_list[word.lower()])
            else:
                cleaned_doc.append(word)
        self.doc = ' '.join(cleaned_doc)

    def remove_numbers_fun(self):
        """
        This function uses regex to remve
        all the numbers from the doc.
        """
        self.doc = re.sub("[0-9]", "", self.doc)

    def remove_html_tags_fun(self):
        """
        This function uses regex's complile method
        to remove all the HTML tags from the doc
        """
        cleaner = re.compile('<.*?>')
        cleaned_text = re.sub(cleaner, '', self.doc)
        cleaned_text = re.sub('[\n\t]', '', cleaned_text)
        self.doc = cleaned_text

    def remove_punctations_fun(self):
        """
        This function uses regex to remove alk the
        punctations from the doc.
        """ 
        self.doc = re.sub('[^a-zA-Z0-9]', ' ', self.doc)

    def lemmatize_fun(self):
        """
        This function applies the stemming to the words
        It can be operated with either WordNetLemmatizer
        or Snowball Stemmer
        ---------------------------
        Example:
        lemmatize(method='snowball')
        
        default value = 'wordnet
        """
        tokens = str(self.doc).split()
        cleaned_tokens = None
        if self.lemmatize_method == 'wordnet':
            cleaned_tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        else:
            cleaned_tokens = [self.lemmatizer.stem(token) for token in tokens]
       
        self.doc = ' '.join(cleaned_tokens)

    def add_stopword(self, *args):
        """
        This function is used to add new stopwords
        to the predefined list
        Parameters - ["new_stopword"]
        ------------------------------
        Example -
        obj = NLP()
        obj.add_stopword(["first_word", "second_word"])
        """
        if self.remove_stopwords is False:
            raise Exception("Please enable removal of stopwords")
        if type(args) != list:
            raise Exception("Error - pass stopwords in list")
        for arg in args:
            self.stopword_list.add(arg)

    def add_replacement(self, *args):
        """
        This function is used to add new replacement words
        to the predifined list
        Parameters - [  = ""]
        ----------------------------
        Example -
        obj = NLP()
        obj.add_replacement([first: "replacement1", second: "replacement2"])
        """
        if self.replace_words is False:
            raise Exception("Please enable cleaning of stopwords")
        if type(args) != list:
            raise Exception("Error - pass input parameters in list")
        if args == []:
            raise Exception("Error - list is empty")
        try:
            for key, value in args.items():
                self.replacement_list[key] = value
        except:
            print("Expected args in dict format")

    def remove_stopwords(self, *args):
        """
        This function is used to remove stopwords from predefined list
        Parameters - ["first_word"]
        ------------------------------
        Example
        obj = NLP()
        obj.remove_stopwords(['new_stopword_here'])

        """
        if self.remove_stopwords is False:
            raise Exception("Error - enable stopword removal functionality")
        if type(args) != list:
            raise Exception("Error - expected a list")
        if args == []:
            raise Exception("Error - no items to remove from stopword list")
        for arg in args:
            if arg in self.stopword_list:
                self.stopword_list.remove(arg)
            else:
                raise Exception(arg+" not in list")

    def print_stopwords(self):
        """
        This function prints all the stopwords
        that are present in the list
        Return Type - list
        ------------------------------
        Example
        obj = NLP()
        obj.print_stopwords()
        """
        if self.stopword_list == []:
            raise Exception("Error - stopword list is empty")
        print(self.stopword_list)

    def process(self, doc):
        """
        This function processes the doc
        If the remove_stopwords flag is True
            - it will remove stopwords from doc
        If the clean_words flag is True
            - it will clean the doc by replacing words
        Parameters - [doc]
        ------------------------------
        Example
        obj = NLP()
        obj.process(["process this text"])

        How to use with pandas?
        obj = NLP()
        df = df['text].apply(obj.process)
        """
        self.doc = doc
        if self.replace_words is True:
            self.replace_words_fun()
        if self.remove_html_tags is True:
            self.remove_html_tags_fun()
        if self.remove_stopwords is True:
            self.remove_stopwords_fun()
        if self.remove_numbers is True:
            self.remove_numbers_fun()
        if self.remove_punctations is True:
            self.remove_punctations_fun() 
        if self.lemmatize is True:
            self.lemmatize_fun()
        return self.doc

