
class AbstractDatabase:
    description = ('pybiodata')
    def __init__(self):
        pass

    @classmethod
    def set_command_arguments(cls):
        import argparse
        parser = argparse.ArgumentParser(description=cls.description)
        parser.add_argument('database', choices=['PDB',], help='set database')
        return parser
