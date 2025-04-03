html_dictionnary = {
    "div": ("<div>", "</div>"),
    "i": ("<i>", "</i>"),
    "b": ("<b>", "</b>"),
    "p": ("<p>", "</p>"),
    "em": ("<em>", "</em>")
}

current_dictionnary = {
    "div": [],
    "i": [],
    "b": [],
    "p": [],
    "em": []
}

def strHTML(strParam):
    first_or_last_string_correct = True
    current_string = ""
    param_list = []
    key_error = ""

    if strParam.startswith("</"):
        first_or_last_string_correct = False

    for i in strParam:
        if i == "<":
            current_string = i
        elif i == ">":
            current_string += i
            param_list.append(current_string)
        else:
            current_string += i

    for cle, value in html_dictionnary.items():
        for j in value:
            for i in param_list:
                if i == j:
                    if not i in current_dictionnary[cle]:
                        current_dictionnary[cle].append(i)
                        param_list.remove(i)

    for cle, value in current_dictionnary.items():
        if len(value) == 1:
            key_error = cle

    if len(param_list) >= 1:
        strParam = "false"
    elif first_or_last_string_correct == False:
        strParam = "false"
    elif not key_error == "":
        strParam = key_error
    elif len(param_list) == 0 and first_or_last_string_correct == True and key_error == "":
        strParam = "true"

    print(current_dictionnary)
    
    return strParam

print(strHTML(input()))