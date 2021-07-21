PATH_TO_FILE = "./f8_shop/assets/css/base.css"
PATH_TO_NEW_FILE = "./f8_shop/assets/css/new_base.css"

import re

with open(PATH_TO_FILE, 'r') as f:
    with open(PATH_TO_NEW_FILE, 'a') as nf:
        print(f.readline())

        def rem_to_px(str_rem):
            str_rem = str_rem.group(1)
            ret = f"line-height: {str(float(str_rem[:-2]) / 10)}rem"
            return ret

        def convert(line):
            line = re.sub(r'line-height: ([0-9]+.?[0-9]*px)', rem_to_px, line)
            return line

        while True:
            line = f.readline()
            if line == '':
                break
            new_line = convert(line)
            nf.write(new_line)
