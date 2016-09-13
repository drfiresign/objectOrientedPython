class Student():
    name = 'Dylan'

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Dylan')
