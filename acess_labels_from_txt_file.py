def generateLabelList(path):
    label_dictionary = {}
    a_file = open(path)
    for line in a_file:
        key, value = line.split()
        label_dictionary[key] = value


    labels = list(label_dictionary.values())
    print(labels)
