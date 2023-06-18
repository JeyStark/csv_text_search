# -*- coding: utf-8 -*-
import os
import csv

def search_text_in_csv(directory, search_text):
    csv.field_size_limit(10 * 1024 * 1024)  # Increase the field size limit to 10 MB

    # Create a new CSV file to store the results
    result_csv = "results.csv"
    with open(result_csv, "w") as result_file:
        csv_writer = csv.writer(result_file)
        csv_writer.writerow(["CSV File", "Line Number", "Content"])

        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".csv"):
                    full_path = os.path.join(root, file)
                    with open(full_path, "r") as csv_file:
                        csv_reader = csv.reader(csv_file)
                        line_number = 0
                        for row in csv_reader:
                            line_number += 1
                            for field in row:
                                if search_text.lower() in field.lower():
                                    csv_writer.writerow([file, line_number, field])
                                    print("Text found in: {}, Line: {}".format(full_path, line_number))
                                    break

main_directory = 'PATH_TO_YOUR_MAIN_FOLDER'
search_text = 'TEXT_TO_FIND'

search_text_in_csv(main_directory, search_text)
