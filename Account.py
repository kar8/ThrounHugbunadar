class Account(object):
    def __init__(self, credit, deposit):
        self.credit = credit
        self.deposit = deposit


    def getName(self):
        return self.__class__.__name__

    def transfer(self, amount):
        self.credit += amount


# Inherits from Account
class Heidursmerki(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.042
        self.indexed = False
        self.fixed = 0.33
        self.monthly = True
        super(Heidursmerki, self).__init__(credit, deposit)


# Inherits from Account
class Sparileid36(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.017
        self.indexed = True
        self.fixed = 36
        self.monthly = True
        super(Sparileid36, self).__init__(credit, deposit)


# Inherits from Account
class Sparileid48(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.018
        self.indexed = True
        self.fixed = 48
        self.monthly = True
        super(Sparileid48, self).__init__(credit, deposit)


# Inherits from Account
class Sparileid60(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.019
        self.indexed = True
        self.fixed = 60
        self.monthly = True
        super(Sparileid60, self).__init__(credit, deposit)


# Inherits from Account
class Vaxtasproti(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.036
        self.indexed = False
        self.fixed = 0
        self.monthly = False
        super(Vaxtasproti, self).__init__(credit, deposit)


# Inherits from Account
class Vaxtathrep(Account):
    def __init__(self, credit, deposit):
        if (credit < 1000000):
            self.interest = 0.032
        elif (credit < 5000000):
            self.interest = 0.036
        elif (credit < 20000000):
            self.interest = 0.039
        elif (credit < 75000000):
            self.interest = 0.042
        else:
            self.interest = 0.045
        self.indexed = False
        self.fixed = 0.33
        self.monthly = True
        super(Vaxtathrep, self).__init__(credit, deposit)


# Inherits from Account
class Fastvaxtareikningur1(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.0392
        self.indexed = False
        self.fixed = 1
        self.monthly = True
        super(Fastvaxtareikningur1, self).__init__(credit, deposit)


# Inherits from Account
class Fastvaxtareikningur3(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.0491
        self.indexed = False
        self.fixed = 3
        self.monthly = True
        super(Fastvaxtareikningur3, self).__init__(credit, deposit)


# Inherits from Account
class Fastvaxtareikningur6(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.0506
        self.indexed = False
        self.fixed = 6
        self.monthly = True
        super(Fastvaxtareikningur6, self).__init__(credit, deposit)


# Inherits from Account
class Fastvaxtareikningur12(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.0538
        self.indexed = False
        self.fixed = 12
        self.monthly = True
        super(Fastvaxtareikningur12, self).__init__(credit, deposit)



if __name__ == "__main__":
    account = Heidursmerki(1000,100)
        
