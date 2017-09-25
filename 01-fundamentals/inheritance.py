# Udacity full-stack web developer nanodegree
# 01. Programming fundamentals and the web
# Lesson 10. Make Classes: Advanced Topics


class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor called.")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)


# Normally the child instance would be in a separate file.
# Included here for ease of demonstration.
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor called.")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    # 01_11: method overriding
    # the child instance of show_info will override the parent instance.
    def show_info(self):
        print("Eye Color - " + self.eye_color)
        print("Last Name - " + self.last_name)


billy_cyrus = Parent("Cyrus", "blue")
print(billy_cyrus.last_name)
billy_cyrus.show_info()

miley_cyrus = Child("Cyrus", "blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)
miley_cyrus.show_info()
