
class circle:

    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return round(3.1415 * self.radius ** 2, 2)

    def calc_hekef(self):
        return round(2 * 3.1415 * self.radius, 2)

    def __str__(self):
        return f'The circle characteristics:\n----------------------------\nradius - {self.radius},' \
               f'\narea: {self.calc_area()},\nhekef - {self.calc_hekef()}.'


print(circle(5))
print()
print(f'The hekef is: {circle(4).calc_hekef()}')
print()
print(f'Tre area is : {circle(6).calc_area()}')
