import sys, mytimer
from _ast import ListComp

reps = 100000
repslist = range(reps)

def forLoop():
    res = []
    for i in repslist:
        res.append(abs(i))
    return res

def listComp():
    return [abs(i) for i in repslist]

def mapCall():
    return map(abs, repslist)

def genExpr():
    return list(abs(i) for i in repslist)

def genFunc():
    def gen():
        for i in repslist:
            yield abs(i)
    return list(gen())

if __name__ == "__main__":
    print sys.version
    for test in (forLoop, listComp, mapCall, genExpr, genFunc) :
        elapsed, result = mytimer.timer(test)
        print '_ ' * 33
        print "%-9s:%.5f => [%s...%s]" %(test.__name__, elapsed, result[0], result[-1])   
         