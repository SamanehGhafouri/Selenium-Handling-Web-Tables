# Polymorphism with Inheritance
# the method flight() is used in all classes but different signature

class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class Sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")


class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly")


if __name__ == '__main__':

    obj_bird = Bird()
    obj_spr = Sparrow()
    obj_ost = Ostrich()

    obj_bird.intro()
    obj_bird.flight()

    obj_ost.intro()
    obj_ost.flight()

    obj_spr.intro()
    obj_spr.flight()


