# Create a method in the Animal class.
# Insert a function that prints the animal's name and sound,
# and execute it on the a1 object.

class animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"the {self.name} goes {self.sound}")

p1 = animal("tiger","zooo")
p1.make_sound()