from __future__ import annotations
import time
from src.features.linguistic import linguistic_features
from src.features.readability import readability_features
from src.features.vocabulary import vocabulary_features
from src.services.feedback_service import indicators,feedback
from src.services.model_service import ModelService

class ScoringService:
    def __init__(self,model_service:ModelService): self.model_service=model_service
    def score(self,text:str):
        start=time.perf_counter(); l=linguistic_features(text); r=readability_features(text); v=vocabulary_features(text); dims=indicators(text); strengths,improvements=feedback(text)
        raw=self.model_service.predict(text) if self.model_service.loaded else None
        elapsed=(time.perf_counter()-start)*1000
        return {"score":{"raw":round(raw,3) if raw is not None else None,"display":round(raw,1) if raw is not None else None,"normalized":round((raw-1)/5*100) if raw is not None else None},"uncertainty":self._interval(raw),"dimensions":dims,"statistics":{"words":int(l["word_count"]),"characters":int(l["char_count"]),"sentences":int(l["sentence_count"]),"paragraphs":int(l["paragraph_count"]),"avg_sentence_length":round(l["avg_sentence_length"],2),"unique_words":int(v["vocabulary_size"]),"lexical_diversity":round(v["lexical_diversity"]*100,1)},"readability":r,"strengths":strengths,"improvements":improvements,"model":{"name":"essayiq-hybrid","version":"1.0.0","trained":self.model_service.loaded},"latency_ms":round(elapsed,2)}
    @staticmethod
    def _interval(raw):
        if raw is None:return {"lower":None,"upper":None,"method":"unavailable_until_model_training"}
        return {"lower":round(max(1,raw-.5),2),"upper":round(min(6,raw+.5),2),"method":"conservative_model_interval_placeholder_until_calibrated"}
