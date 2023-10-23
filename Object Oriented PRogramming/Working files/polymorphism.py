class Bird:

    def intro(self):
        print('This is a bird!')

    def flight(self):
        print('Most birds can fly!')


class Sparrow(Bird):
    def flight(self):
        print('Sparrow can fly!')


bird = Bird()
sparrow = Sparrow()
bird.flight()
sparrow.intro()
sparrow.flight()
