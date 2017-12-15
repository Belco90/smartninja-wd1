from datetime import datetime


class Person(object):

    def __init__(self, fn, ln, ema, pn, by):
        self.first_name = fn
        self.last_name = ln
        self.email = ema
        self.phone_number = pn
        self.birth_year = by

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_age(self):
        now = datetime.now()
        return now.year - self.birth_year


john = Person("John", "Clark", "john@clark.com", 89348239429, 1979)
marissa = Person(fn="Marissa", ema="marissa@yahoo.com", ln="Mayer", pn=12342, by=1988)
david = Person(fn="David", ema="david@yahoo.com", ln="Mayer", pn=111, by=1978)

contacts = [john, marissa, david]

for item in contacts:
    print item.get_full_name()
    print item.get_age()
    print item.phone_number
    print item.birth_year
    print item.email
    print ""
