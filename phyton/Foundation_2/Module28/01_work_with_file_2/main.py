class Newopen:
    def __init__(self, filename:str, filemode:str = 'r'):
        self._filename = filename
        self._mode = filemode
    def __enter__(self):
        try:
            self.my_file = open(self._filename, self._mode)
        except Exception:
            self.my_file = open(self._filename, 'w')
        return self.my_file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.my_file.close()
        return True

with Newopen('test2.txt') as testfile:
    testfile.write('dfdf')
