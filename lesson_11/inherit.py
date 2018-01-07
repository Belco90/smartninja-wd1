class Dad(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name + " " + self.last_name


class Mother(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name + ", " + self.last_name


class Son(Dad, Mother):
    def __init__(self, first_name, last_name, toy):
        super(Son, self).__init__(first_name, last_name)
        self.toy = toy

    def details(self):
        return self.full_name() + " " + self.toy


david = Dad(first_name="David", last_name="Beltran")
johnny = Son(first_name="Johnny", last_name="Brown", toy="Tractor")

print david.full_name()
print johnny.full_name()

# -------------------------------------------


class Felino(object):

    def maullar(self):
        return "grrr"


class Guepardo(Felino):
    def maullar(self):
        return super(Guepardo, self).maullar() + 'rrrrrrrrr'

