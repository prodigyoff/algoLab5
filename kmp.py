def find_prefixes(pattern: str, pattern_length: int, prefix_list: list) -> list:
    length = 0
    pattern_counter = 1
    while pattern_counter < pattern_length:
        if pattern[pattern_counter] == pattern[length]:
            prefix_list[pattern_counter] = length + 1
            length += 1
            pattern_counter += 1
        else:
            if length != 0:
                length = prefix_list[length - 1]
            else:
                prefix_list[pattern_counter] = 0
                pattern_counter += 1
    return prefix_list


def kmp(pattern: str, text: str):
    if not text or not pattern or len(pattern) > len(text):
        return -1
    pattern_length = len(pattern)
    prefix_list = [0] * pattern_length
    find_prefixes(pattern, pattern_length, prefix_list)
    text_counter = 0
    pattern_counter = 0
    result = []
    while text_counter < len(text):
        if text[text_counter] == pattern[pattern_counter]:
            text_counter += 1
            pattern_counter += 1
        else:
            if pattern_counter != 0:
                pattern_counter = prefix_list[pattern_counter - 1]
            else:
                text_counter += 1
        if pattern_counter == pattern_length:
            result.append((text_counter - pattern_counter, text_counter - 1))
            pattern_counter = prefix_list[pattern_counter - 1]
    return result
