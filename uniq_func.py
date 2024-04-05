def uniq_func(list_in):
    list_out = []
    for i_dict in list_in:
        if i_dict not in list_out:
            list_out.append(i_dict)
    return list_out


# def uniq_func(list_in):
#     set_in = set()
#     print(list_in)
#     set_in.union(set(list_in))
#     return list(set_in)


list_for_exm = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]

print(uniq_func(list_for_exm))
