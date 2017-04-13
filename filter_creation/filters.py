import re


def parse_matrix(match):

    output_str = ""
    vision_type = match.group('vision_type')
    output_str += vision_type
    for color in ['red', 'green', 'blue']:
        output_str += ", "
        color_list = match.group(color).split(", ")
        color_list = [str(0.01 * float(x)) for x in color_list]
        color_str = ', '.join(color_list)
        output_str+= color_str
    output_str += "\n"
    return output_str

def parse_file():
    pattern = r'(\w+)\D*(\d+\.[\d])\D*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)\W*\n'

    pattern2 = r'(?P<vision_type>\w+)\D*\[(?P<red>.*, .*, .*)\]\D*\[(?P<green>.*, .*, .*)\]\D*\[(?P<blue>.*, .*, .*)\]'


    with open("raw_filter.txt", 'r') as f:
        result = []
        # result = re.findall(pattern2, f.read())
        for line in f:
            result.append(re.search(pattern2, line))
        return result

def main():
    parsed_file = parse_file()

    with open("filter_matrices.csv", 'w') as f:
        for line in parsed_file:
            f.write(parse_matrix(line))


main()
