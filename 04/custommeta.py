class CustomMeta(type):
    def __new__(mcs, name, bases, init_dic):

        new_dict = {
             (("custom_" + key), key)
             [key.startswith('__') and
              key.endswith('__')]: init_dic[key]
             for key in
             init_dic.keys()
         }
        
        new_dict["__setattr__"] = lambda ex, attr, val: ex.__dict__.update({("custom_" + attr) if not attr.startswith("__") and not attr.endswith("__") else attr: val})
        return super().__new__(mcs, name, bases, new_dict)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
