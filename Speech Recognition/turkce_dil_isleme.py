from turkishnlp import detector

obj = detector.TurkishNLP()
obj.download()
obj.create_word_set()
lwords = obj.list_words("vri kümsi idrae edre ancak daha güezl oaflbiler")
print(obj.auto_correct(lwords))