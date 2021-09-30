def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    file = open(csv_file_path, "rw+")
    lines=file.read(-1)
    lines=lines.split('\n')
    for row in range(len(lines)):
        lines[row]=(lines[row]).split(',')
        for column in range(len(lines[row])):
            if isdigit(lines[row][column]):
                lines[row][column]=(int) (lines[row][column])
    return lines
