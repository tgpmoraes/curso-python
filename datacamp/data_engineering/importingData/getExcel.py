import pandas as pd


file_path = 'Streamlined-Data-Ingestion-with-pandas-Datacamp-main'
excel_file = f'../{file_path}/fcc-new-coder-survey.xlsx'
survey_responses = pd.read_excel(excel_file,
                                 skiprows=2)

# View the head of the data frame
print(survey_responses.head())

# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel(excel_file,
                               skiprows=2,
                               sheet_name=1)

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
print(job_prefs.head())


# Load all sheets in the Excel file
all_survey_data = pd.read_excel(excel_file,
                                skiprows=2,
                                sheet_name=None)

# View the sheet names in all_survey_data
print(all_survey_data.keys())

# Create an empty data frame
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in all_survey_data.values():
    # Print the number of rows being added
    print("Adding {} rows".format(df.shape[0]))
    # Append df to all_responses, assign result
    all_responses = all_responses.append(df)

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
print(counts.head())

# Count NA values in each column
print(all_responses.columns)

# Load file with Yes as a True value and No as a False value
# survey_subset = pd.read_excel("fcc_survey_yn_data.xlsx",
#                               dtype={"HasDebt": bool,
#                               "AttendedBootCampYesNo": bool},
#                               true_values=['Yes'],
#                               false_values=['No'])

# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel(excel_file,
                            skiprows=2,
                            dtype={'Part1StartTime': 'datetime64'})

# Print first few values of Part1StartTime
# print(survey_data.Part1StartTime.head())

# # Create dict of columns to combine into new datetime column
# datetime_cols = {"Part2Start": ['Part2StartDate', 'Part2StartTime']}


# # Load file, supplying the dict to parse_dates
# survey_data = pd.read_excel("fcc_survey_dts.xlsx",
#                             parse_dates=datetime_cols)

# # View summary statistics about Part2Start
# print(survey_data.Part2Start.describe())

# Parse datetimes and assign result back to Part2EndTime
# survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"],
#                                              format="%m%d%Y %H:%M:%S")

# # Print first few values of Part2EndTime
# print(survey_data.Part2EndTime.head())
