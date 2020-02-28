VOCABULARY = ['dog', 'cheese', 'cat', 'mouse']
TEXT = 'the mouse eat the cheese'
 
def to_bow(text):
    words = text.split(" ")
    return [1 if w in words else 0 for w in VOCABULARY]
 
print(to_bow(TEXT))  # [0, 1, 0, 1]