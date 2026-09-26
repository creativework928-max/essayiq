from __future__ import annotations
from src.features.linguistic import linguistic_features
from src.features.vocabulary import vocabulary_features
from src.features.grammar import grammar_features
from src.features.structure import structure_features

def indicators(text:str):
    l=linguistic_features(text); v=vocabulary_features(text); g=grammar_features(text); s=structure_features(text)
    grammar=100.0
    grammar-=min(45,g["repeated_word_signals"]*4+g["repeated_punctuation_signals"]*8+g["spacing_anomalies"]*3+g["capitalization_anomalies"]*3+g["fragment_signals"]*2)
    vocab=min(100,max(0,50+v["lexical_diversity"]*50))
    org=min(100,max(0,55+s["transition_word_frequency"]*5-(s["paragraph_length_std"]/(s["avg_paragraph_length"]+1))*25))
    readability=min(100,max(0,100-abs(l["avg_sentence_length"]-20)*2))
    content=min(100,max(0,50+v["rare_word_signal"]*30+l["word_count"]**0.5))
    return {"content":round(content),"grammar":round(grammar),"organization":round(org),"vocabulary":round(vocab),"readability":round(readability)}

def feedback(text:str):
    l=linguistic_features(text); g=grammar_features(text); v=vocabulary_features(text); s=structure_features(text); strengths=[]; improvements=[]
    if v["lexical_diversity"]>=.55: strengths.append("The essay demonstrates relatively varied vocabulary.")
    if g["repeated_word_signals"]==0: strengths.append("No immediate adjacent repeated-word pattern was detected.")
    if s["transition_word_frequency"]>=2: strengths.append("Several explicit transition signals are present.")
    if l["avg_sentence_length"]>28: improvements.append("Several sentences are unusually long; consider splitting complex ideas.")
    if g["repeated_punctuation_signals"]>0 or g["spacing_anomalies"]>0: improvements.append("Review repeated punctuation and spacing patterns.")
    if s["transition_word_frequency"]<2 and l["paragraph_count"]>1: improvements.append("Consider adding clearer transitions between paragraphs where appropriate.")
    if not strengths: strengths.append("The analysis did not identify a strong positive signal above the configured thresholds.")
    if not improvements: improvements.append("No major rule-based improvement signal crossed the configured threshold; human review is still recommended.")
    return strengths,improvements
