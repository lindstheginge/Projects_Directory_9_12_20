    def cylinder_volume(r, h):
        r_squared = r * r
        volume = r_squared * h * 3.14
        return volume

if __name == "__main__":
    radius = int(input("Enter in radius: "))
    height = int(input("Enter in height: "))
    volume = cylinder_volume(radius, height)
    print("The volume is: ", volume)


    def get_square_root(x):
        x_squared = x * x
        return x_squared

if __name == "__main__":
    x = int(input("Enter number to find the square root of: "))
    x_squared = get_square_root(x)
    print("The square root of ", x, "is: ", x_squared)
