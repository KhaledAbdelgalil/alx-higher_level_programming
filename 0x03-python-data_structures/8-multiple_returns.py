#!/usr/bin/python3
def multiple_returns(sentence):
    result = ()
    if not sentence:
        result = 0, None
    else:
        result = len(sentence), sentence[0]
    return result
