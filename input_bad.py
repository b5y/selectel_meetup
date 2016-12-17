def cc_bad():
    res = 0
    for i in xrange(10):
        for j in xrange(i):
            for k in xrange(5):
                for l in xrange(k):
                    for m in xrange(10):
                        res += k + i + j + l + m
    return res
