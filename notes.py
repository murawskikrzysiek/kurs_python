total = sum


def above_average(l):
    mean = total(l) / len(l)
    return [x for x in l if x > mean]


def print_formated(text, length=20, side="right"):
    print("{:{side}{width}}".format(text, side=">" if side.lower() == "right" else "<", width=length))


def get_input_text():
    lines_of_text = []
    while True:
        line = input("Input text line: ")
        if not line:
            break
        lines_of_text.append(line)
    return lines_of_text


def get_input_and_print_formated(side="right", length=20):
    text = get_input_text()
    print("".join([str(i % 10) for i in range(1, length+1)]))
    for line in text:
        print_formated(line, length=length, side=side)


def cat_replacer(file_to_cat):
    with open(file_to_cat, "r") as f:
        for line in f:
            print(line, end="")


def sort_replacer(file_to_sort):
    with open(file_to_sort, "r") as f:
        for line_id, line in enumerate(sorted(f)):
            print("{line_id}: {text}".format(line_id=line_id, text=line), end="")


def fibonacci(count=10, _first=0, _second=1):
    return ([_first] + fibonacci(count=count-1, _first=_second, _second=_first + _second)) if count != 0 else []


class Prostokat():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "a: {a}, b: {b}".format(a=self.a, b=self.b)

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return 2 * self.a + 2 * self.b

if __name__ == '__main__':
    # lista = range(1001)
    # l_total = total(lista)
    # print(l_total)
    # print(above_average(lista))
    # print(print_formated_to_right(text="test"))
    # print(get_input_text())
    # sort_replacer("test_file.txt")
    # print(fibonacci(40))
    P = Prostokat(2, 3)
    print(P.a)
    print(P.b)
    print(P.pole())
    print(P.obwod())
    print(P)
