# Family Tree Program

# Family relationships
father = {
    'john': 'david',
    'john': 'lisa',
    'david': 'robert',
    'david': 'mary'
}

mother = {
    'susan': 'david',
    'susan': 'lisa',
    'anna': 'robert',
    'anna': 'mary'
}


# Find father
def find_father(person):
    for f, child in father.items():
        if child == person:
            return f
    return "Not Found"


# Find mother
def find_mother(person):
    for m, child in mother.items():
        if child == person:
            return m
    return "Not Found"


# Find parents
def find_parent(person):
    result = []

    f = find_father(person)
    m = find_mother(person)

    if f != "Not Found":
        result.append(f)

    if m != "Not Found":
        result.append(m)

    return result


# Find siblings
def find_siblings(person):
    result = []

    parents = find_parent(person)

    for parent in parents:
        for child in father.values():
            if child != person and child not in result:
                if parent in find_parent(child):
                    result.append(child)

        for child in mother.values():
            if child != person and child not in result:
                if parent in find_parent(child):
                    result.append(child)

    return result


# Main Program
print("FAMILY TREE")

name = input("Enter person's name: ").lower()

print("Father:", find_father(name))
print("Mother:", find_mother(name))
print("Parents:", find_parent(name))
print("Siblings:", find_siblings(name))
