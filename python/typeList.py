x = ['magical unicorns',19,'hello',98.98,'world']

if x is int:
    if test >= 100:
        print "That's a big number!"
    else:
        print "That's a small number!"
elif x is str:
    if len(test) >= 50:
        print "Long sentence."
    else:
        print "Short sentence."
elif isinstance(test, list):
    if len(test) >= 10:
        print "Big list!"
    else: 
        print "Short list." 