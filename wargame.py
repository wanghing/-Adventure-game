import random
import time


def print_stop(message):
    print(message)
    time.sleep(1)


def validate_input(asking, option1, option2):
    while True:
        choice = input(asking)
        if "1" in choice:
            return choice
            break
        if "2" in choice:
            return choice
            break


def intro(weapon, enemy):
    print_stop("You are holding " + weapon + " inside a castle.")
    print_stop("Your target is to defeat the enemy before your"
               " castle being destroyed")
    print_stop("The enemy is coming. It's a " + enemy + " .")


def action(weapon, enemy):
    castle_protection = 5
    if enemy == "tank":
        remaining_power = 80
    elif enemy == "helicopter":
        remaining_power = 40
    print_stop("The remaining power of the enemy is " +
               str(remaining_power))
    while castle_protection > 0 and remaining_power > 0:
        choice = validate_input("Please choose to attack or change weapon\n"
                                "Machinegun has lower attack power"
                                " with higher chance to hit\n"
                                "Cannon has higher attack power with"
                                " lower chance to hit\n"
                                "Enter 1 to change weapon\n"
                                "Enter 2 to attack\n", "1", "2")
        if "1" in choice:
            if weapon == "machine gun":
                weapon = "cannon"
            elif weapon == "cannon":
                weapon = "machine gun"
        print_stop("You are holding " + weapon + " now.")
        if "2" in choice:
            remaining_power = remaining_power_of_enemy(weapon, enemy,
                                                       remaining_power)
        castle_protection -= 1
        print_stop("The castle protection reduced to " +
                   str(castle_protection))
    if remaining_power <= 0:
        print_stop("You win. You defeated the enemy")
    elif castle_protection == 0:
        print_stop("Castle destroyed. You loss!")


def remaining_power_of_enemy(weapon, enemy, remaining_power):
    if hit_or_not(weapon, enemy):
        remaining_power -= power_weapon(weapon)
        print("Hit the enemy!")
    else:
        print("Missed the target")
    print("Remaining power of enemy is" + str(remaining_power) + " .")
    return remaining_power


def power_weapon(weapon):
    if weapon == "machine gun":
        return 20
    elif weapon == "cannon":
        return 30


def hit_or_not(weapon, enemy):
    if enemy == "tank":
        if weapon == "machine gun":
            return True
        elif weapon == "cannon":
            return True
    elif enemy == "helicopter":
        if weapon == "machine gun":
            return True
        elif weapon == "cannon":
            if random.randint(0, 10) > 6:
                return True
            else:
                return False


def game():
    weapon = "machine gun"
    enemylist = ["tank", "helicopter"]
    enemy = random.choice(enemylist)
    intro(weapon, enemy)
    action(weapon, enemy)
    choice = validate_input("Play again?\n"
                            "Enter 1 to play again\n"
                            "Enter 2 to quit\n", "1", "2")
    if "1" in choice:
        game()
    if "2" in choice:
        print_stop("Goodbye!")


game()
