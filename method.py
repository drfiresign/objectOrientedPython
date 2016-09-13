class Store():
    open = 9
    close = 10

    def hours(self):
        return "We're open from {} to {}.".format(self.open, self.close)
