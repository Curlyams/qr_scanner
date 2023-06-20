import re 


def clean_data(data_list):
    delims = "-", " "
    regex_pattern = '|'.join(map(re.escape, delims))
    scan_clean = []

    for data in data_list:
        try:
            split_data = re.split(regex_pattern, data)
            if len(split_data) >= 4:
                # Keep only the first 4 items in split_data
                split_data = split_data[:4]
                scan_clean.append(split_data)
            else:
                missing_cols = 4 - len(split_data)
                split_data.extend(['ScanError'] * missing_cols)
                scan_clean.append(split_data)
        except Exception as e:
            print(f"Error cleaning data: {data}. {str(e)}. Skipping...")

    return scan_clean
