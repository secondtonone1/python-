import socket
from io import StringIO
import sys
class TypeClass(object):
    def typeprint(self, name = 'typeclass'):
        print('class name is %s' %(name))

typeclasses = TypeClass()
print(type(TypeClass))
print(type(typeclasses))

def printHW(self):
    print('Hello world!!!')
TypeClass2 = type('TypeClass2', (object,), dict(typeprinthw = printHW))
typeclass2 = TypeClass2()
typeclass2.typeprinthw()

class DictMetaclass(type):
    def __new__(cls, name, bases, attrs):
        def insertattr(self,key, value):
            self[key]=value
        attrs['insert'] = insertattr
        return type.__new__(cls, name, bases, attrs)

class MyDict(dict, metaclass = DictMetaclass):
    pass

mydict = MyDict()
mydict.insert('nice', 3)
print(mydict['nice'])

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['insert'] = lambda self, value: self.append(value)
        return type.__new__(cls,name,bases,attrs)

class Mylist(list,metaclass = ListMetaclass):
    pass

mylist = Mylist()
mylist.insert('name')
mylist.insert('age')
print(mylist)


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s%s>' %(self.__class__.__name__, self.name)

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField,self).__init__(name, 'bigint')

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name,'varchar(100)')

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if  name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Founc model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping: %s ==> %s' %(k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings2__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict , metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s' " %key)
    def __setattr__(self, key, value):
        self[key]=value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings2__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

#错误用法，因为Model没有mappings
'''
u = Model(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
'''


















