from tasks import *

def test_vocabulary_builder():
    t2i, i2t = make_vocabulary_map([text])
    assert all(i2t[t2i[tok]] == tok for tok in t2i), "something wrong with translation dicts"
