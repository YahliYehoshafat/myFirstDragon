from Pet import Pet


def eat(pet: Pet) -> None:
    """
    
    Update pet parameters according to the eating actions
    """
    pet.change_hunger(10)
    pet.change_energy(5)
    pet.change_happiness(5)
    pet.change_points(10)
    pet.add_history_action("eat")
    print("Your animal ate food!")


def sleep(pet: Pet) -> None:
    """
    
    Update pet parameters according to the sleeping actions
    """
    pet.change_energy(10)
    pet.change_happiness(5)
    pet.change_points(10)
    pet.add_history_action("sleep")
    print("Your animal went to sleep!")


def play(pet: Pet) -> None:
    """
    
    Update pet parameters according to the playing actions
    """
    pet.change_happiness(10)
    pet.change_energy(-7)
    pet.change_hunger(-3)
    pet.change_points(10)
    pet.add_history_action("play")
    print("Your animal played!")


def get_pet_state(pet: Pet) -> None:
    """
    
    Prints pet's state
    """
    print(f"animal name = {pet.name}\nanimal type = {pet.type}\nanimal hunger = {pet.hunger}\npoints = {pet.points}")
    print(f"animal energy = {pet.energy}\nanimal happiness = {pet.happiness}\nanimal history = {str(pet.history)}")


def calaulate_pet_profile(pet: Pet) -> int:
    """
    
    Calculate animal state
    """
    return (pet.energy + pet.happiness + pet.hunger) / 3