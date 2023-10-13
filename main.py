class Animal:
    def __init__(self, name, date_of_birth, commands):
        self.name = name
        self.date_of_birth = date_of_birth
        self.commands = commands

    def get_info(self):
        return f"Name: {self.name}, Date of Birth: {self.date_of_birth}, Commands: {self.commands}"

class Dog(Animal):
    def __init__(self, name, date_of_birth, commands):
        super().__init__(name, date_of_birth, commands)
        self.animal_type = "Dog"

class Cat(Animal):
    def __init__(self, name, date_of_birth, commands):
        super().__init__(name, date_of_birth, commands)
        self.animal_type = "Cat"

class Hamster(Animal):
    def __init__(self, name, date_of_birth, commands):
        super().__init__(name, date_of_birth, commands)
        self.animal_type = "Hamster"

class Horse(Animal):
    def __init__(self, name, date_of_birth, commands):
        super().__init__(name, date_of_birth, commands)
        self.animal_type = "Horse"

class Camel(Animal):
    def __init__(self, name, date_of_birth, commands):
        super().__init__(name, date_of_birth, commands)
        self.animal_type = "Camel"

class Donkey(Animal):
    def __init__(self, name, date_of_birth, commands):
        super().__init__(name, date_of_birth, commands)
        self.animal_type = "Donkey"

class DomesticAnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        for animal in self.animals:
            print(animal.get_info())

class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.count > 0:
            raise ValueError("Resource not properly managed in a try-with-resources block")

def main():
    registry = DomesticAnimalRegistry()

    while True:
        print("Animal Registry Menu:")
        print("1. Add a new animal")
        print("2. List animals")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            with Counter() as counter:
                name = input("Enter the name of the animal: ")
                date_of_birth = input("Enter the date of birth (YYYY-MM-DD): ")
                commands = input("Enter commands (comma-separated): ")

                animal_type = input("Enter animal type (Dog, Cat, Hamster, Horse, Camel, or Donkey): ")
                if animal_type == "Dog":
                    animal = Dog(name, date_of_birth, commands)
                elif animal_type == "Cat":
                    animal = Cat(name, date_of_birth, commands)
                elif animal_type == "Hamster":
                    animal = Hamster(name, date_of_birth, commands)
                elif animal_type == "Horse":
                    animal = Horse(name, date_of_birth, commands)
                elif animal_type == "Camel":
                    animal = Camel(name, date_of_birth, commands)
                elif animal_type == "Donkey":
                    animal = Donkey(name, date_of_birth, commands)
                else:
                    print("Invalid animal type.")
                    continue

                registry.add_animal(animal)
                counter.add()
                print("Animal added to the registry.")

        elif choice == "2":
            print("List of Animals in the Registry:")
            registry.list_animals()

        elif choice == "3":
            print("Exiting the Animal Registry.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
