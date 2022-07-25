

from datetime import date


d = date(2012, 12, 21)

print(format(d))


print(format(d,'%A, %B %d, %Y'))

print('The end is {:%d %b %Y}. Goodbye'.format(d))