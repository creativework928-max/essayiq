from src.features.linguistic import linguistic_features
from src.features.vocabulary import vocabulary_features
from src.features.grammar import grammar_features
from src.features.readability import readability_features

def test_linguistic_counts():
    d=linguistic_features("Hello world. This is a test!")
    assert d["word_count"]==6
    assert d["sentence_count"]==2

def test_vocabulary():
    d=vocabulary_features("word word test")
    assert d["vocabulary_size"]==2
    assert 0<d["lexical_diversity"]<=1

def test_grammar_signals():
    assert grammar_features("This this works!!!")["repeated_word_signals"]==1
    assert grammar_features("This this works!!!")["repeated_punctuation_signals"]==1

def test_readability_returns_expected_keys():
    d=readability_features("This is a simple sentence. Another simple sentence follows here.")
    assert "flesch_reading_ease" in d
