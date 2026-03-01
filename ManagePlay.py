from Pet import Pet
from PetsOptins import PetsOptions
from Actions import eat, sleep, play, get_pet_state, calaulate_pet_profile


def manage_play() -> None:
    """
    
    Manages the animal care game
    :param optins: Action option
    :param pet: Pet object
    """
    try:
        print("Welcome to the big animal game!!!")
        pet = create_new_animal()
        while True:
            option: str = "start value"
            while not option.isdigit() or int(option) > 5 or int(option) < 1:
                print("Please select an action:\n1)Sleep\n2)Eat\n3)Play\n4)Get pet state\n5)Get animal profile")
                option = input()
            match int(option):
                case 1:
                    sleep(pet)
                case 2:
                    eat(pet)
                case 3:
                    play(pet)
                case 4:
                    get_pet_state(pet)
                case 5:
                    print(calaulate_pet_profile(pet))
            print()
    except KeyboardInterrupt:
        print("\nBye bye :(")
        exit()


def create_new_animal() -> Pet:
    """
    
    Create an animal object
    :param pet_name: Pet name
    :param pet_type: Pet type
    """
    pet_name: str = ""
    while pet_name == "":
        pet_name = input("please type your pet's name: ")
    pet_type:str = "start value"
    while not pet_type.isdigit() or int(pet_type) > 3 or int(pet_type) < 1:
        print("Choose an animal type from the following options:\n1)Cat\n2)Dog\n3)Dolphin")
        pet_type = input()
    match int(pet_type):
        case 1:
            pet_type = PetsOptions.CAT.value
        case 2:
            pet_type = PetsOptions.DOG.value
        case 3: 
            pet_type = PetsOptions.DOLPHIN.value
    return Pet(pet_name, pet_type)


if __name__ == "__main__":
    manage_play()