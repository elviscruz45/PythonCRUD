_formats = {
        'ymd' : '{d.year}-{d.month}-{d.day}',
        'mdy' : '{d.month}/{d.day}/{d.year}',
        'dmy' : '{d.day}/{d.month}/{d.year}'}

class Date:
    def __init__(self, year, month, day):
                self.year = year#2012
                self.month = month#12
                self.day = day#21
    def __format__(self,casa):

        casa = 'mama'
        return casa

d = Date(2012, 12, 21)

print(format(d))
