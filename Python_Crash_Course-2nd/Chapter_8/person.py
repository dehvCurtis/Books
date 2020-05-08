
def build_person(first_name,last_name,age=None):
    """ Return a dict of info about person """
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age

    return person

skater = build_person('tony','hawk')
print(skater)