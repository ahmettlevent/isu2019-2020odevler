import docclass
cl = docclass.classifier(docclass.getwords)
cl.train('the quick brown fox jumps over the lazy dog', 'good')
cl.train('make quick money in the online casino', 'bad')
print (cl.fcount('quick', 'good'))
print (cl.fcount('quick', 'bad'))
print (cl.categories())
print (cl.catcount("bad"))
print (cl.catcount("good"))
print (cl.fprob('quick','good'))
print (cl.fprob('quick','bad'))
print (cl.fprob('money','bad'))
print (cl.fprob('money','good'))
print (cl.fprob('the','good'))
print (cl.fprob('the','bad'))
print (cl.fprob('brown','good'))
print (cl.fprob('online','good'))
print (cl.fprob('online','bad'))
print (cl.weightedprob("online", "bad",cl.fprob))
print (cl.weightedprob("online", "good", cl.fprob))


cl = docclass.naivebayes(docclass.getwords)
docclass.sampletrain(cl)
print (cl.prob('quick rabbit','good'))
print (cl.prob('quick rabbit','bad'))

print (cl.prob('quick money','good'))
print (cl.prob('quick money','bad'))

print (cl.prob('Bu duzgun ve anlamli bir e posta midir?','bad'))
print (cl.prob('Bu duzgun ve anlamli bir e posta midir?','good'))

print (cl.classify('quick rabbit'))
print (cl.classify('quick money'))

print (cl.classify_with_thresholds('quick rabbit'))
print (cl.classify_with_thresholds('quick money'))


