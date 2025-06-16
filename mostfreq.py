def most_freq_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0

        count[char] += 1
    print(count)

    best = 'None'

    for char in s:
        if best is None or count[char] > count[best]:
            best = char
    return best


most_freq_char('sssruthi')


############
# Time: O(n)
# Space: O(n)
