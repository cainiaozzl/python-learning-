class Fruit(object):

  """A class that makes various tasty fruits."""

  def init(self, name, color, flavor, poisonous):

    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):

    print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

  def is_edible(self):

    if not self.poisonous:
      print "Yep! I'm edible."
    else:
      print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()

lemon.is_edible()


class Triangle(object):
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3



class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg

my_car = Car("DeLorean", "silver", 88)
print my_car.model
print my_car.color
print my_car.mpg
