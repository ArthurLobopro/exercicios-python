def notas(*notes, sit=False):
    quant = len(notes)
    DICTIONARY = {
        "quant": quant,
        "média": sum(notes) / quant,
        "min": min(*notes),
        "max": max(*notes)
    }

    if sit:
       DICTIONARY["sit"] = situacao(DICTIONARY["média"])

    return DICTIONARY

def min(*values):
    min_value = values[0]
    for value in values:
        if value < min_value:
            min_value=value
    
    return min_value

def max(*values):
    max_value = values[0]
    for value in values:
        if value > max_value:
            max_value=value
    
    return max_value

def situacao(media):
    if media >=7:
        return "Bom"
    
    if media >= 5:
        return "Razoável"
    
    return "Ruim"

notes = notas(4,7.5,6,9, sit=True)
print(notes)