# Call Log Analysis

This repository contains a Python script `call.py` that analyzes call logs stored in a text file. The script utilizes the pandas library to read and process the call logs data.

## Requirements

To run this script, you need to have the following:

- Python 3.x

- pandas library

## Usage

1. Place the call logs text file (`call_logs.txt`) in the same directory as the `call.py` script.

2. Open a terminal or command prompt and navigate to the directory containing `call.py`.

3. Run the script using the following command:

   ```

   python call.py

   ```

   The script will read the call logs file, perform calculations, and display the results on the console.

## Functionality

The `call.py` script performs the following actions:

1. Reads the call logs text file into a pandas DataFrame.

2. Removes leading spaces from column names in the DataFrame.

3. Sets the `CONTACT` variable to a specific value (to filter the DataFrame by a specific contact).

4. Retrieves the `LOCAL` ID from the first row of the DataFrame.

5. Filters the DataFrame to include only rows with the specified contact ID.

6. Calculates the total duration of calls with the specific contact (excluding missed calls).

7. Calculates the number of calls made to the specific contact (excluding missed calls).

8. Prints the date range of the call logs.

9. Prints the number of calls made to the specific contact (excluding missed calls).

10. Converts the total call duration from seconds to hours.

11. Prints the total duration of calls made to the specific contact in seconds and hours.

12. Calculates and prints the total duration in days, hours, minutes, and seconds.

Please note that you need to modify the `CONTACT` variable in the script to specify the contact ID you want to analyze.

Feel free to explore the code and adapt it to your specific use case or modify it as needed.

## License

This repository is licensed under the [MIT License](LICENSE).
