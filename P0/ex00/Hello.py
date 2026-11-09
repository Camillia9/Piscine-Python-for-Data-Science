def main():
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}

    # On parcourt une list avec un index
    ft_list[1] = "World"

    # Un tuple est non modifiable. On cree un nouveau tuple
    ft_tuple = (ft_tuple[0], "France")

    # Un set n'a pas d'index. Suppression et ajout. Set ne garantit pas l'ordre des elements
    ft_set.remove("tutu!")
    ft_set.add("Paris")

    # On accede a la valeur d'un dictionnaire grace a sa cle ({cle: valeur})
    ft_dict["Hello"] = "42Paris"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)

if __name__ == '__main__':
    main()