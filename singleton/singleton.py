class OnlyOne(object):
    class __OnlyOne:
        def __init__(self):
            self.val = None
        def __str__(self):
            return 'self' + self.val
    instance = None
    def __new__(cls):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne()
        return OnlyOne.instance
    def __getattr__(self, name):
        return getattr(self.instance,name)
    def __setattr__(self, name):
        return setattr(self.instance,name)

x = OnlyOne()
x.val = "name1"

y = OnlyOne()
y.val = "name2"

z = OnlyOne()
z.val = "name3"

print(x)
print(y)
print(z)

