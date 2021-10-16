# неуверен что правильно понял задачу, но  сделал как понял.
#search for annotations
def sea_annot(text, word):
    a = open(text, "r")
    b = ""
    c = []
    for line in a:
        b = b + line
    a.close()
    b = b.replace('\n', "")
    b = b.split(".")
    for i in b:
        i = i.split("!")
    #  в принципе можно еще и цикл для разбивки по "?" сделать, логика такаяже.
    for j in b:
        if j.startswith(word) or j.endswith(word) or " " + word + " " in j:
            c.append(j)
    a.close()
    return print(c)

sea_annot("text.txt", "est")




# раскладывать  лист до цыфр через фильтр не имеет смысла итоговая  сумма будет меньше

g = [9, 22, 23, 9, 45, 654]
u = 996544520


def addition(x):
    s = 0
    if isinstance(x, int):
        while x > 0:
            s += x % 10
            x //= 10
        return print("Сумма отдельных цыфр числа  =", "\033[31m {}" .format (s))
    if isinstance(x, list):
        for i in range(len(x)):
            s += g[i]
        return print("\033[0m{}".format ("Сумма отдельных цыфр числа ="), "\033[31m {}" .format (s))


addition(u)
addition(g)
