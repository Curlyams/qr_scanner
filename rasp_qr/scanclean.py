import re 


def clean_data(data_list):
    delims = "-", " "
    regex_pattern = '|'.join(map(re.escape, delims))
    scan_clean = [re.split(regex_pattern, n) for n in data_list]

    for n in scan_clean:
        n[3:5] = [' '.join(n[3:5])]

    return scan_clean
