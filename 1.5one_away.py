def one_edit(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    non_exis_chars = []
    if str1_len == str2_len:
        for x in str1:
            if x not in str2:
                non_exis_chars.append(x)
                print(non_exis_chars)
                if len(non_exis_chars) > 1:
                    return False

    if str1_len < str2_len:
        for x in str2:
            if x not in str1:
                non_exis_chars.append(x)
                if len(non_exis_chars) > 1:
                    return False
    if str1_len > str2_len:
        for x in str1:
            if x not in str2:
                non_exis_chars.append(x)
                if len(non_exis_chars) > 1:
                    return False
    return True


data = [('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)]

for x, y, z in data:
    k = one_edit(x, y)
    if k == z:
        print("pass")
    else:
        print("fail")

# print(one_edit())
