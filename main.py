# main.py
from pet import Pet

if __name__ == "__main__":
    my_pet = Pet("Cupcake")
    my_pet.get_status()

    my_pet.eat()
    my_pet.play()
    my_pet.get_status()

    my_pet.sleep()
    my_pet.get_status()

    my_pet.train("Roll Over")
    my_pet.train("Shake Paw")
    my_pet.show_tricks()