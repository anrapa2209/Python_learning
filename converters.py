def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45

#breaks down code into multiple files called modules, i.e., organizable structures to make it reusable
#we can take the above 2 functions &put them into a separate module called converters
#& then, we can import that module into any program that needs these converter functions