# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 03:02:28 2023

@author: myrin
"""


import Glassdoor_scraper as gs 

import pandas as pd

path= r"C:\Users\myrin\Documents\ds_salary_proj\chromedriver"

df = gs.get_jobs('data scientist' , 1500 , False , path , 15)

df.to_csv('glassdoor_jobs.csv' , index = False)
