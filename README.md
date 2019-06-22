# NLPUTILS

NLPUTILS is a preprocessing package for NLP task. The main objective of the package is to reduce time consumed for preprocessing by using ready made functions.

# Requirements

 * Python 3.4 or higher

# Installation

 ### Using PIP via PyPI
 ```
 $ pip install nltutils
 ```

 ### Manually via GIT
 ```
 $ git clone git://github.com/gaganmanku96/nlputils
 $ cd nlputils
 $ python setup.py install
 ```

# Functionalities
1. Replaces words
2. Remove stopwords
3. Remove numbers
4. Remove HTML tags
5. Remove punctations

# Usage
```
>>> from nlpuitls import NLPUTILS()
>>> obj = NLPUTILS
```
 ## Parameters
 ```
 >>> obj = NLPUTILS(
        replace_words=True,
        remove_stopwords=True,
        remove_numbers=True,
        remove_HTML_tags=True,
        remove_punctation=True
        )
 ```
 ## Using with Pandas Library
 ```
 >>> dataFrame['text'] = dataFrame['text].apply(obj.process)

 ```
 ## Using with plain textx
 ```
 >>> print(obj.process("Pass a text here"))
 ```
 ## Add more stopwords
 ```
 >>> obj = NLPUTILS()
 >>> obj.add_stopword(['this', 'and this'])
 ```
 ## Add more replace words
 ```
 >>> obj = NLPUTILS()
 >>> obj.add_replacement([this="by this", this="by this"])
 ```

 
