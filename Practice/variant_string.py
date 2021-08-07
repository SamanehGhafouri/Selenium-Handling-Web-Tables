global count
count = 0
def variant(final_list: list, given_list: list, distinct_variant: set):
    # given_list[:] = st
    if len(given_list) == 0:
        global count
        count += 1
        # distinct_variant.add(" ".join(final_list))
        print(" ".join(final_list))
        return
    else:
        for i in range(len(given_list)):
            copy_given_list = given_list.copy()
            char = copy_given_list.pop(i)
            variant(final_list + [char], copy_given_list, distinct_variant)


if __name__ == '__main__':
    w = "Hel"
    list_w = []
    list_w[:] = w
    set_var = set()
    result = variant([], list_w, set_var)
    print(result)
    print(count)
    print(set_var)
    print(len(set_var))

