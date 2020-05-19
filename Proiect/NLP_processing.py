import nltk
import clips
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize

def preprocess(sents):
    lmtzr = WordNetLemmatizer()
    lemmatized = [[lmtzr.lemmatize(word) for word in word_tokenize(s)]
                  for s in sents]
    punctuation=[",",".","!","?",":",";","..."]
    lemmatized_witout_p=[[word for word in lemmatized[i] if not word in punctuation] for i in range(0,len(lemmatized))]
    return lemmatized_witout_p

def get_S_M_P(sents):
    #POS TAGGING
    lemmatized_witout_p = [nltk.pos_tag(i) for i in sents]

    P = list()
    S = list()
    M = list()

    for word in lemmatized_witout_p[2]:
        if(word[1]) in ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$']:
            if word in lemmatized_witout_p[0]:
                P.append(word)
            elif word in lemmatized_witout_p[1]:
                S.append(word)

    for word in lemmatized_witout_p[0]:
        if (word[1]) in ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$']:
            if word in lemmatized_witout_p[1] and not word in lemmatized_witout_p[2]:
                M.append(word)

    return (S,M,P)

def searchnegative(lista):
    negation = False
    neg_list = ["none", "no", "not", "neither"]
    for i in lista:
        if i.lower() in neg_list:
            negation = not negation
    if negation is False:
        return "positive"
    else:
        return "negative"


def searchquantifier(lista):
    quantifier = "universal"
    universal = ["all", "every", "any", "each"]
    particular = ["some", "most", "few", "plenty", "several"]
    for i in lista:
        if i.lower() in particular:
            quantifier = "particular"
        elif i.lower in universal:
            quantifier = "universal"
    return quantifier

def get_middle_letter(sentence):
    quantifier = searchquantifier(sentence)
    negation = searchnegative(sentence)
    if quantifier == "universal":
        if negation == "positive":
            return "a"
        else:
            return "e"
    else:
        if negation == "positive":
            return "i"
        else:
            return "o"

def get_premise_types(sents):
    processed_sents = preprocess(sents)
    for index, i in enumerate(processed_sents):
        if index == 0:
            letter = get_middle_letter(i)
            major_premise = "M" + letter + "P"
        elif index == 1:
            letter = get_middle_letter(i)
            minor_premise = "S" + letter + "M"
        else:
            letter = get_middle_letter(i)
            conclusion = "S" + letter + "P"
    return (major_premise, minor_premise, conclusion)

