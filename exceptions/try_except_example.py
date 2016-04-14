'''
Try and except:

In computer programs errors occur. This is expected. It is normal.
But if something unexpected happens, it is exceptional—and an exception is thrown.
'''

# import module sys to get the type of exception.

import sys

while True:
    try:
        value = int(input('Enter an integer:'))
        result = 1/value
        break
    except:
        print 'Oops!', sys.exc_info()[0], 'occured.'
        print

print 'The reciprocal of', value, 'is', result