from tasks import *

def test_token_counts():
    text = """The quick brown fox jumps over the lazy dog. The fox and the dog play together. 
              The fox chases the dog, but the dog runs quickly. The fox is fast, and the dog escapes."""
    expected = {'the': 9, 'quick': 1, 'brown': 1, 'fox': 4, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 5, 
                'and': 2, 'play': 1, 'together': 1, 'chases': 1, 'but': 1, 'runs': 1, 'quickly': 1, 
                'is': 1, 'fast': 1, 'escapes': 1}
    obtained = token_counts(text)
    assert type(obtained) == dict, "expected return type 'dict'"
    assert set(obtained.keys()) == set(expected.keys()), "unexpected keys in dict"
    assert all(obtained[key] == expected[key] for key in expected), "unexpected counts"
