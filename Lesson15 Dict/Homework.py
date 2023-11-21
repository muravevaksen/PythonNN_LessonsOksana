def to_alternating_case(string):
    return(string.swapcase())

print(to_alternating_case('hello world'))

def get_planet_name(id):
    dict = {1: "Mercury", 2: "Venus", 3: "Earth", 4: "Mars",
            5: "Jupiter", 6: "Saturn", 7: "Uranus", 8: "Neptune"}
    return dict[id]

print(get_planet_name(5))