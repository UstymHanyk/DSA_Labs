def get_prefix_list(needle):
    prefix_values = [0] * len(needle)
    matched_chars = 0

    for current_index, char in enumerate(needle[1:], 1):
        while matched_chars > 0 and needle[matched_chars] != char:
            matched_chars = prefix_values[matched_chars - 1]
        if needle[matched_chars] == needle[current_index]:
            matched_chars += 1
        prefix_values[current_index] = matched_chars

    return prefix_values


def kmp_search(haystack, needle):
    if not needle:
        return [0]

    needle_length = len(needle)
    prefix_values = get_prefix_list(needle)
    matched_chars = 0
    indices = []

    for current_index, current_char in enumerate(haystack):
        while matched_chars > 0 and needle[matched_chars] != current_char:
            matched_chars = prefix_values[matched_chars - 1]
        if needle[matched_chars] == current_char:
            matched_chars += 1
        if matched_chars == needle_length:
            indices.append(current_index - needle_length + 1)
            matched_chars = prefix_values[matched_chars - 1]

    return indices
