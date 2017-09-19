#-*-coding:utf-8-*-
## try except

class Dict(dict):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except Exception as e:
            raise AttributeError('AttributeError is :%s', e)
    def __setattr__(self, key, value):
        self[key] =  value




