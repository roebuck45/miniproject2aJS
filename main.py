# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# INF601 - Advanced Programming in Python
# Joshua Seirer
# Mini Project 2a

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata
from configs import APIToken, cdcPWD

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cdc.gov",
                 APIToken,
                 username="j_seirer@mail.fhsu.edu",
                 password=cdcPWD)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cdc.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("nt65-c7a7", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

print(results_df)

# (5/5 points) Proper import of packages used.

# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or

# retrieve some data for creating basic statistics on. This will generally come in as json data, etc.

# Think of some question you would like to solve such as:
#   NCHS - Injury Mortality: United States
#   https://dev.socrata.com/foundry/data.cdc.gov/nt65-c7a7

# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data
# is labeled tabular data.
# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build
# some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder,
# the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt
# file which contains all the packages that need installed. You can create this fille with the output of pip freeze at
# the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install
# the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on
# the explanations.