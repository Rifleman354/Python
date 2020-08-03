def planetRegister2(name, segmentum, pop=''):
    """Generates information about a planet"""
    if pop:
        planet_info = "Planet " + name + " is located in segmentum " + segmentum + "; population: " + str(pop)
    else:
        planet_info = "Planet " + name + " is located in segmentum " + segmentum + "."
    return planet_info