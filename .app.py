word1 = ["you","much","hard"]
word2 = ["i","you","he"]
word3 = ["love","ate","works"]
result = map(lambda x,y,z : f "{x},{y},{z}", word2, word3,word1)
for i in result
    print(list(result))