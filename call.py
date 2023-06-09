import pandas as pd

# Read the text file into a DataFrame
df = pd.read_csv(
    "call_logs.txt", parse_dates=["Time of call"], sep="\s*,\s*", engine="python"
)

# Remove leading spaces from column names
df.columns = df.columns.str.strip()

CONTACT = "+989303501392"

LOCAL = df["Local ID"].iloc[0]


filtered_df = df[df["Contact ID"] == CONTACT]

# Calculate the total duration of calls with the specific number
total_duration = filtered_df["Duration"].sum()

# Calculate the total duration of calls with the specific number
total_duration = filtered_df[filtered_df["Direction"] != "Missed"]["Duration"].sum()

# Calculate the number of calls (excluding missed calls)
num_calls = len(filtered_df[filtered_df["Direction"] != "Missed"])


min_date = filtered_df["Time of call"].min().date()
max_date = filtered_df["Time of call"].max().date()

print(f"From {min_date} to {max_date}")

print(f"Number of calls (excluding missed calls): {num_calls}")

# Convert the total duration from seconds to hours
total_duration_hours = total_duration / 3600

# Print the total duration
print(
    f"Total duration of calls between +{LOCAL} & {CONTACT}: {total_duration} seconds, equivalent to {total_duration_hours:.2f} hours"
)


days = total_duration // 86400
hours = (total_duration % 86400) // 3600
minutes = (total_duration % 3600) // 60
seconds = (total_duration % 3600) % 60

print("=== === === === === === ===")
print(f"Or {days} days, {hours} hours, {minutes} minutes, {seconds}seconds")
