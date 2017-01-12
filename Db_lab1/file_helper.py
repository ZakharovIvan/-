
from pickle import dump
from pickle import load

class file_helper:
    @staticmethod
    def dump_to_file(table, fname):
        file = open(fname, 'wb')
        dump(table, file)
        file.close()

    @staticmethod
    def load_from_file(fname):
        try:
            file = open(fname,'rb')
        except:
            return {}
        return load(file)

    @staticmethod
    def clean_file(fname):
        file = open(fname, 'wb')
        file.close()
