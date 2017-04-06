
# -*- coding: utf-8 -*-
""" 
Author: Abdelrahman Khaled Hussen
Date: 4/2/2017

"""

import string
from itertools import chain

from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag

from pywsd.cosine import cosine_similarity as cos_sim
from pywsd.utils import lemmatize, porter, lemmatize_sentence, synset_properties

EN_STOPWORDS = stopwords.words('english')

"""
    This is the implementation of Michael E.Lesk 1986.
    It uses only the senses definition to compare it with the words in the neighbourhood (surrounding text).
    """
def original_lesk(neighbourhood, Targetword):
    dictionary={}
    Targetword = lemmatize(Targetword)
    for synset in wn.synsets(Targetword):
        definition = synset_properties(synset, 'definition')
        dictionary[synset] = definition
    Result = compare_overlaps_original_lesk(neighbourhood.split(), dictionary)
    return Result    
	 
"""
    Calculate overlaps between the context sentence and the sense definition
    and returns the sense with the highest overlap.(Used with Original Lesk only.
    """
def compare_overlaps_original_lesk(sentence, dictionary):
    max = 0
    Ranked_sense = None
	
    for synset in dictionary:
        overlaps = set(dictionary[synset]).intersection(sentence)
        if len(overlaps) > max:
            Ranked_sense = synset
            max = len(overlaps)    
    return Ranked_sense
	  
"""
       Calculates overlaps between the context sentence and the synset signture(Lemmas ,Definitions and Examples)
    and returns a ranked list of synsets from highest overlap to lowest.
    
    """

def compare_overlaps_simple_lesk(sentence, synsets_sign):
   
    overlaplen_synsets = [] # a tuple of (len(overlap), synset).
    for ss in synsets_sign:
        overlaps = set(synsets_sign[ss]).intersection(sentence)
        overlaplen_synsets.append((len(overlaps), ss))

    # Rank synsets from highest to lowest overlap.
    ranked_synsets = sorted(overlaplen_synsets, reverse=True)

    # Returns only the best sense.
    return ranked_synsets[0]

    """ 
    Returns a synsets_signatures dictionary that includes signature synset of a 
    sense consisting of its:
    (i)   definition
    (ii)  example sentences
    (iii) lemmas
    """
def synset_signature(Targetword, pos=None):

    synsets_signatures = {}
    for synset in wn.synsets(Targetword):
        # If POS is specified.
        if pos and str(synset.pos()) != pos:
            continue
        signature = []
        # Includes definition.
        definition = synset_properties(synset, 'definition')
        signature+=definition
        # Includes examples
        examples = synset_properties(synset, 'examples')
        signature+=list(chain(*[i.split() for i in examples]))
        # Includes lemma_names.
        lemma_names = synset_properties(synset, 'lemma_names')
        signature+= lemma_names
        # Includes lemma_names of hypernyms and hyponyms.
        hyponyms = synset_properties(synset, 'hyponyms')
        hypernyms = synset_properties(synset, 'hypernyms')
        hypohypernyms = hypernyms+hyponyms
        signature+= list(chain(*[i.lemma_names() for i in hypohypernyms]))
        # Removes stopwords.
        signature = [i for i in signature if i not in EN_STOPWORDS]
        # Lemmatized context is preferred over stemmed context.
        signature = [lemmatize(i) for i in signature]
        # Matching exact words may cause sparsity, so optional matching for stems.
        signature = [porter.stem(i) for i in signature]
        synsets_signatures[synset] = signature

    return synsets_signatures

    """
    Simple Lesk uses the synset signature (definitions.examples and lemmas) and compare it with the surrounding text.
	And like the Original Lesk it returns the highest overlap between the synset signature and the sentence
    """
def simple_lesk(sentence,Targetword,pos=None,sentence_is_lemmatized=False):

    # Ensure that ambiguous word is a lemma.
    Targetword = lemmatize(Targetword)
    # Get the signatures for each synset.
    ss_sign = synset_signature(Targetword, pos)
    # Disambiguate the sense in context.
    if sentence_is_lemmatized:
        sentence = sentence.split()
    else:
        sentence = lemmatize_sentence(sentence)
    highest_overlap = compare_overlaps_simple_lesk(sentence, ss_sign)
    return highest_overlap
