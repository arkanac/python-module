
def healing_potion():
    try:
        from .elements import create_fire, create_water
    except ImportError as e:
        print(e)
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion():
    try:
        from .elements import create_fire, create_earth
    except ImportError as e:
        print(e)
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion():
    try:
        from .elements import create_air, create_water
    except ImportError as e:
        print(e)
    return f"Invisibility potion brewed with {create_air()} and \
            {create_water()}"


def wisdom_potion():
    try:
        from .elements import create_fire, create_water, create_air, \
            create_earth
    except ImportError as e:
        print(e)
    all_four_results = [create_fire(), create_water(), create_earth(),
                        create_air()]
    return f"Healing potion brewed with {all_four_results}"
