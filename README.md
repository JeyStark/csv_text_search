# csv_text_search
csv_text_search is a Python tool that allows you to search for specific text within CSV files. It provides a simple and efficient way to explore large CSV datasets and extract relevant information.




Usage

Clone the repository or download the csv-text-search.py file.

Open a terminal or command prompt.

Navigate to the directory where the csv-text-search.py file is located.

Run the script with Python:

    python csv_text_search.py "YOUR_PATH_TO_MAIN_FOLDER" TEXT_TO_FIND

Real example:

    python csv_text_search.py "/home/myData" "Iron Man"


The script will search for the specified text within the CSV files and generate a results.csv file containing the matched lines, including the CSV file name and line number.

Example

Suppose you have a directory structure as follows:
- data
  - file1.csv
  - file2.csv
  - subdirectory
    - file3.csv
   
You want to search for the text "Iron Man" within these CSV files. You would run the script, provide the path to the data directory as the main directory, and enter "example" as the search text. The script will search for "example" within all the CSV files in the data directory and its subdirectories, and generate a results.csv file with the matched lines.

Contributing

Contributions, bug reports, and feature requests are welcome. Feel free to open an issue or submit a pull request.

Enjoy searching through your CSV files effortlessly with csv_text_search!
