def practice_with_list():
    print("\nPracticing with lists . . .")  # \n for new line
    scores = list()
    scores.append(100)
    scores.append(50)
    scores.append(100)
    scores.append(75)
    print("the list is: ", scores)
    scores.sort()
    print("sort ascending: ", scores)
    scores.reverse()
    print("sort descending:", scores)
    print("length: ", len(scores))
    print("number of 100s: ", scores.count(100))
    print("lowest score: ", min(scores))
    print("highest score: ", max(scores))
    input("\nEnter any key to continue: ")


practice_with_list()  # call it to see it


def practice_with_tuple():
    print("\nPracticing with tuples . . .")
    days = ("Mon", "Tue", "Wed", "Thur", "Fri")
    print("tuple is", days)
    print("printing each day: ")
    for x in days:  # x can be any valid variable name - meaningful helps sometimes
        print(x)
    print("\nlength: ", len(days))
    print("index for Mon:", days.index("Mon"))
    print("first word alphabetically", min(days))
    print("last word alphabetically", max(days))
    input("\nEnter any key to continue: ")


practice_with_tuple()


def practice_with_string():
    print("\nPracticing with strings . . .")
    s = "sphinx of black quartz judge my vow"  # has all 26 letters too!
    print("num of chars is", len(s))
    words = s.split()
    print("num of words is: ", len(words))
    print("now printing words in alphabetical order: ")
    words.sort()
    for word in words:
        print(word)
    input("\nEnter any key to continue: ")


practice_with_string()


def practice_with_dictionary():
    print("\nPracticing with dictionaries...")
    print("Let's enter 3 names and gpas.")
    students = dict()
    for x in range(3):
        name = input("Enter name: ")
        gpa = input("Enter " + name + "'s " + "gpa: ")
        students[name] = gpa
    print("dictionary is", students)
    print("number of pairs ", len(students))
    for k in students.keys():
        print(k, " had a gpa of: ", students.get(k))
    print("Lowest gpa is: ", min(students.values()))
    print("Highest gpa is: ", max(students.values()))
    gpas = list(students.values())
    gpas.sort()
    print("gpas sorted is ", gpas)
    struct = []
    for k, v in students.items():
        struct.append([v, k])
    struct.sort()
    print("Printing in sorted order:")
    for x in struct:
        print(x[0], "earned by ", x[1])
    input("\nEnter any key to continue: ")


practice_with_dictionary()
