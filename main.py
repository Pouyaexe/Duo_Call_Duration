# app for getting your Google Duo Call history and tells you how much is the total duration
# Made by Pouya


from functools import total_ordering

import pandas as pd

# import data from history.txt into a dataframe


def txt_to_df():
    df = pd.read_csv("history.txt")
    return df


df = txt_to_df()


# Now select the rows that have a specific value in the column Contact ID (AKA the phone number)
from target_numbers import list_of_numbers as target_number

df_selected = df[df[" Contact ID"].isin(target_numbers)]

# Lets see what is the total duration of the calls

# Exporting the data to a .txt file


def export_to_txt(df):
    df.to_csv("history_selected.txt", index=False)
    return df


export_to_txt(df_selected)

total = df_selected[" Duration"].sum()


# Convert the total duration to hours, minutes and seconds
def total_duration(total):
    hours = total // 3600
    minutes = (total % 3600) // 60
    seconds = (total % 3600) % 60
    return hours, minutes, seconds


# First row Time of call and last row Time of call
print("________________________________________________")

print(
    "From "
    + df_selected["Time of call"].iloc[0]
    + " to "
    + df_selected["Time of call"].iloc[-1]
    + ": \n"
)
# Print the first row's ' Local ID' and target_numbers
print("Between ", df_selected[" Local ID"].iloc[0], " and ", target_numbers, ": \n")

print("hours, minutes, seconds", total_duration(total), "\n")
# Or in days, hours, minutes and seconds


def total_duration_days(total):
    days = total // 86400
    hours = (total % 86400) // 3600
    minutes = (total % 3600) // 60
    seconds = (total % 3600) % 60
    return days, hours, minutes, seconds


print("Or days, hours, minutes, seconds", total_duration_days(total))

# Lets see how many calls were made

print("________________________________________________")

print(
    "There were ",
    len(df_selected[df_selected[" Direction"] != " Missed"]),
    " calls made",
)
# Avarage number of calls in each day
