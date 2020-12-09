if __name__ == "__main__":
    def get_user_name():
        name = input("Enter your name: ")
        return name

    def get_user_age():
        age = input("Enter your age: ")
        return age

    def name_and_age():
        print(get_user_name(), get_user_age())

    name_and_age()
