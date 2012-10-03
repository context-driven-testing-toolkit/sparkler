import sys

if len(sys.argv) > 1:

    print 'sys.argv:' 
    print sys.argv

else:

    # for multiline input:
    print 'sys.stdin.readlines()'
    print sys.stdin.readlines()
