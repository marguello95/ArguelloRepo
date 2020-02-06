list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

#Creating list for common words
def common_words(list_a,list_b):
    results =[]
    for i in list_a:
        if i in list_b:
            results.append(i)
    return results
print "Words that occur in both lists:" , ( common_words(list_a,list_b))

#Creating list for uncommon words
def uncommon_words(list_a,list_b):
    results2 =[]
    for i in list_a:
        if not i in list_b:
            results2.append(i)
    return results2
print "Words that do not Overlap" , ( uncommon_words(list_a,list_b))
