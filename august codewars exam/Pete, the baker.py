def cakes(recipe, available):
    arr = []
    for value in recipe:
        for value2 in available:
            if value not in available:
                return 0
            elif type(value) != int and value == value2:
                arr.append(available[value2] // recipe[value])
            else:
                continue
                
    return min(arr) if len(arr) > 0 else 0        