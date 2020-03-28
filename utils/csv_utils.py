import csv


def write_csv(list_to_write, header, file_path):
    """A function to write a list to a CSV file"""
    with open(file_path, mode="w") as csv_file:
        writer = csv.writer(csv_file, delimiter=";", quotechar='"')
        writer.writerow(header)
        writer.writerows(list_to_write)
