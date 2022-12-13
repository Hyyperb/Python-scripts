class cout:
    def __lshift__(self, other):
        print(other,end='')

class cin:
    def __rshift__(self,other):
        input(other)

cout = cout()
cin = cin()
endl = "\n"


cin>>"enter you name";
cout<<"Hello, world!";
