import numpy as np
from src.models.hybrid_model import build_hybrid

def test_hybrid_model_can_fit_small_sample():
    texts=["Education helps society learn and grow.","Good writing uses clear evidence and structure.","Practice improves communication and reasoning.","Technology can support learning when used carefully.","Reading develops vocabulary and critical thinking.","Students benefit from feedback and revision."]
    y=np.array([3.,4.,4.,5.,5.,4.])
    model=build_hybrid(max_tfidf_features=200)
    model.fit(texts,y)
    pred=model.predict([texts[0]])
    assert 1<=float(pred[0])<=6
