# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 12:49:40 2023

@author: myrin
"""
#importing required librarys
import pandas as pd
import numpy as np

#reading Dataset
df = pd.read_csv(r"C:\Users\myrin\Documents\ds_salary_proj\glassdoor_jobs.csv")

#after looking data  my lisrt to clean data >>

#Salary  parsing
#company name text only
#age of company
#parsing of job description (skills  :- python etc.)

df.columns
"""
Index(['Unnamed: 0', 'Job Title', 'Salary Estimate', 'Job Description',
       'Rating', 'Company Name', 'Location', 'Headquarters', 'Size', 'Founded',
       'Type of ownership', 'Industry', 'Sector', 'Revenue', 'Competitors'],
      dtype='object')
"""

########################## Salary  parsing ################################################
#removing rows in DF having -1 in salary Estimate column
df = df[df['Salary Estimate'] != '-1']

#removing (Glassdoor est.)  in Salary Estimate

salary = df["Salary Estimate"].apply(lambda x:x.split("(")[0])
# we are created new column of salary with no (Glassdoor est.)

#removig $ sign and K i Salary column
minus_kd = salary.apply(lambda x : x.replace("K","").replace("$",""))

#now in Salary Estimate there are some datapoints which having 
#Employer Provided Salary and Salary Per Hour

#so we are making seprate column for hourly jobs
# and creating vatriable 1 for hourly paying  job and 0 for other 
df["hourly"] = df["Salary Estimate"].apply(lambda x : 1 if "per hour" in x.lower() else 0)

#now we go for Employer Provided Salary making new column for it 1 for Employer Provided Salary 0 for else
df["employer_provided"] = df["Salary Estimate"].apply(lambda x :1 if "employer provided salary" in x.lower() else 0)

#now after creating seprate column for Employer Provided Salary and Salary Per Hour
#we are replacing Employer Provided Salary and Salary Per Hour  with nothing > "" in minus_kd salary column

min_hr = minus_kd.apply(lambda x: x.lower().replace("per hour","").replace("employer provided salary:",""))
#now Salary Estimate in min_hr is cleaned

# making seprate column for minimum salary and maximum salary and avarage salary
df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2


############################ company name text  only ##################################

# in DF there are company aname and retting  but we need name only in column

df["company_txt"] = df.apply(lambda x : x["Company Name"] if x["Rating"] > 0 
                                                else x["Company Name"][:-3] , axis  = 1)

############################ state field #############################################

#  in DF column > Locatio we will take only State 
df["Job_state"] = df["Location"].apply(lambda x : x.split(",")[1])

df.Job_state.value_counts()



############################# same state as  v #########################################
df["same_state"] = df.apply(lambda x : 1 if x.Location  == x.Headquarters else 0,axis = 1)


############################## company age  ############################################
# Founded year is  minus from current year 2023 to get company age 
df["age"]  = df.Founded.apply(lambda x : x if x < 1 else 2023 - x)


################### parsing of job description (skills  :- python etc.) ##################

#python 
df["python_yn"] = df['Job Description'].apply(lambda x : 1 if "python" in x.lower() else 0) 
df["python_yn"].value_counts()
"""
1    392
0    350
"""

#r studio
df["R_yn"] = df['Job Description'].apply(lambda x : 1 if "r studio" in x.lower() else 0) 
df["R_yn"].value_counts()
"""
0    741
1      1
"""

#spark
df["spark"] = df['Job Description'].apply(lambda x : 1 if "spark" in x.lower() else 0) 
df["spark"].value_counts()
"""
0    575
1    167
"""

#aws
df["aws"] = df['Job Description'].apply(lambda x : 1 if "aws" in x.lower() else 0) 
df["aws"].value_counts()
"""
0    566
1    176
"""

#asure

df["asure"] = df['Job Description'].apply(lambda x : 1 if "asure" in x.lower() else 0) 
df["asure"].value_counts()
"""
0    662
1     80
"""

#Excel
df["Excel"] = df['Job Description'].apply(lambda x : 1 if "excel" in x.lower() else 0) 
df["Excel"].value_counts()
"""
1    388
0    354
"""
df_out = df.drop(['Unnamed: 0'],axis  = 1)

df_out.to_csv('salary_data_cleaned.csv',index = False)


