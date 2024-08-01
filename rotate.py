#get list and rotate once
def rotate(mod_list: list) -> list:
    mod_list.append(mod_list[0])
    mod_list.pop(0)
    return mod_list