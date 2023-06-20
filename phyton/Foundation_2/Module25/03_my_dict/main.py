class MyDict(dict):
    def get(self, __key):
        __d = super().get(__key)
        if __d == None:
            return 0
        else:
            return __d