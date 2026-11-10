def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif object != object:
        # pcq Nan != Nan, le seul objet qui n'est jamais egale a lui-meme.
        print(f"Cheese: {object} {type(object)}")
    elif type(object) is int and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif object == "":
        print(f"Empty: {type(object)}")
    elif object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0

# Utiliser 'is' pour None, Bool, et type(int, str, list..)
# Utiliser '==' pour les valeurs (12, abc..)

# False = 0. Donc lorsque NULL_not_found(False)
# est appele: s'arrete au print("Zero") car object == 0.
# Pour cela que j'ai rajoute la verif du int.