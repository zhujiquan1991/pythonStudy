try:
    s = None
    if s is None:
        print "s is none"
        raise NameError
    print len(s)
except NameError:
    print "kong hasnt len"