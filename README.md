# Google Duo Call History Analyzer

This repository contains a Python script (`call.py`) that allows you to analyze your Google Duo call history and determine the total duration of calls made to specific phone numbers. The script is developed by Pouya.

## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- Python 3.x

- pandas library

You can install the required packages by running the following command:

```

pip install pandas

```

## Usage

1. Place your Google Duo call history file (`history.txt`) in the same directory as the `call.py` script.

2. Modify the `target_numbers.py` file to include the list of phone numbers you want to analyze. The file should contain a variable called `list_of_numbers`, which should be a list of strings representing the phone numbers.

3. Run the script using the following command:

```

python call.py

```

## Output

The script performs the following actions:

1. Reads the call history data from the `history.txt` file and stores it in a pandas DataFrame.

2. Selects the rows from the DataFrame that correspond to the specified phone numbers.

3. Exports the selected call history data to a new file named `history_selected.txt`.

4. Calculates the total duration of the selected calls and displays it in hours, minutes, and seconds.

5. Calculates the total duration of the selected calls in days, hours, minutes, and seconds.

6. Displays the first and last time of the selected calls.

7. Displays the first row's 'Local ID' and the list of target phone numbers.

8. Displays the number of calls made (excluding missed calls).

9. Calculates the average number of calls made per day.

## Note

Make sure your Google Duo call history file (`history.txt`) follows the required format for the script to work correctly.

Feel free to modify and adapt the script to suit your specific needs.

If you have any questions or suggestions, please contact Pouya.
