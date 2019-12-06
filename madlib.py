
print('Hello and welcome to my Mad lib game!\n'
      'The name of today\'s Mad lib is "Make me a Video Game"')


def file_open(filename):
    """Opens and reads file for madlib template"""
    f = open('madlib.txt', 'r')
    madlib_template = f.read()
    return madlib_template


def collect_answer():
    """Takes in user input, returns array of strings"""
    answers = []
    print("Please enter an adjective:")
    answers.append(str(input()))
    print("Please enter an adjective:")
    answers.append(str(input()))
    print("Please enter a first name:")
    answers.append(str(input()))
    print("Please enter a past tense verb:")
    answers.append(str(input()))
    print("Please enter a a first name:")
    answers.append(str(input()))
    print("Please enter an adjective:")
    answers.append(str(input()))
    print("Please enter an adjective:")
    answers.append(str(input()))
    print("Please enter a plural noun:")
    answers.append(str(input()))
    print("Please enter a large animal:")
    answers.append(str(input()))
    print("Please enter a small animal:")
    answers.append(str(input()))
    print("Please enter a girl's name:")
    answers.append(str(input()))
    print("Please enter an adjective:")
    answers.append(str(input()))
    print("Please enter a plural noun:")
    answers.append(str(input()))
    print("Please enter an adjective:")
    answers.append(str(input()))
    print("Please enter a plural noun:")
    answers.append(str(input()))
    print("Please enter a number, 1 through 50:")
    answers.append(str(input()))
    print("Please enter a first name:")
    answers.append(str(input()))
    print("Please enter a number:")
    answers.append(str(input()))
    print("Please enter a plural noun:")
    answers.append(str(input()))
    print("Please enter a number:")
    answers.append(str(input()))
    print("Please enter a plural noun:")
    answers.append(str(input()))
    return answers


def final_product(filename):
    """'unpacks' user input array and populates template, then prints
    the final madlib"""
    madlib_template = file_open(filename)
    answers = collect_answer()
    final = madlib_template.format(*answers)
    print(final)


final_product('madlib.txt')


def write_madlib(path, contents):
    """Writes completed madlib into new file"""
    with open(path, 'a') as f:
        f.write(contents)


write_madlib('newmadlib.txt', '')
