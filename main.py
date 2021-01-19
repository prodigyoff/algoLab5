from kmp import kmp
import re

INPUT_FILE_LOCATION = 'kmp.in'
OUTPUT_FILE_LOCATION = 'kmp.out'

if __name__ == '__main__':
    with open(INPUT_FILE_LOCATION, 'r') as input_file:
        pattern, text = input_file.readline().split()
    result = kmp(pattern, text)
    print(result)
    with open(OUTPUT_FILE_LOCATION, 'w') as file:
        file.write(str(result))

    # regex solution
    print([(match.start(), match.end() - 1) for match in re.finditer(pattern, text)])
