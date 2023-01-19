# Data Science Salary Estimator: Project :books:
  
* Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.

* Scraped over 1000 job descriptions from glassdoor using python and selenium

* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.

* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.

* Built a client facing API using flask

## Code and Resources Used

__Python Version:__ 3.9

__Packages:__ pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle

__For Web Framework Requirements:__ # `pip install -r requirements.txt`

__Scraper Github:__ https://github.com/arapfaik/scraping-glassdoor-selenium

__Scraper Article:__ https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

__Flask Productionization:__ https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## YouTube Project Walk-Through by Ken Jee >> 

 YouTube >> https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

__Ken Jee's__ GitHub Profile >>> https://github.com/PlayingNumbers

__:heart: :heart: :heart: And big Thank you to Ken Jee  > this is my First end to end project 😊 :blush: :heart: :heart: :heart:__


## Web Scraping

Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:

* Job title

* Salary Estimate

* Job Description

* Rating

* Company

* Location

* Company Headquarters

* Company Size

* Company Founded Date

* Type of Ownership

* Industry

* Sector

* Revenue

* Competitors

## Data Cleaning

After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

* Parsed numeric data out of salary

* Made columns for employer provided salary and hourly wages

* Removed rows without salary

* Parsed rating out of company text

* Made a new column for company state

* Added a column for if the job was at the company’s headquarters

* Transformed founded date into age of company

## Made columns for if different skills were listed in the job description:

* Python

* R

* Excel

* AWS

* Spark

* Column for simplified job title and Seniority

* Column for description length

## EDA

I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.




![company revenue and jobs salary](https://user-images.githubusercontent.com/108168115/210273321-e541be50-6570-4e3f-81e2-fcd4539435ff.png)

![Salary and company age](https://user-images.githubusercontent.com/108168115/210273328-597d39e8-d8e2-446f-842e-f83605946d3b.png)

![state jobs](https://user-images.githubusercontent.com/108168115/210273329-3a69a5d3-e07d-4677-82cb-95710f47959d.png)

![avarage job salary](https://user-images.githubusercontent.com/108168115/210273332-876911cc-58f8-4623-9d2e-e1d17c592712.png)



### skills required 1 yes 0 for no  Python  Excel  AWS




![AWS requirments](https://user-images.githubusercontent.com/108168115/210273333-cee82d26-34da-4b17-a1f6-f756f5f5e9f5.png)

![Excel requirments](https://user-images.githubusercontent.com/108168115/210273323-1a79da2a-5a57-464f-a7fd-a41b7d1bd72a.png)

![Python requirments](https://user-images.githubusercontent.com/108168115/210273326-7891b6a3-a551-40a8-8e41-3aaa6b1b6066.png)



### word cloud of job description 




![word cloud fpr job description](https://user-images.githubusercontent.com/108168115/210273330-6828201d-0a18-44a7-b27b-cd0420b62f99.png)




## Model Building
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly

bad in for this type of model.

### I tried three different models:

*  __Multiple Linear Regression__ – Baseline for the model 

* __Lasso Regression__ – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.

* __Random Forest__ – Again, with the sparsity associated with the data, I thought that this would be a good fit.

## Model performance

The Random Forest model far outperformed the other approaches on the test and validation sets.

* __Random Forest__ : MAE = 11.120102768456377

* __Linear Regression__: MAE = 3919437.2410207116 # 

* __Ridge Regression__ : MAE = 11.120102768456377

## Productionization

In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.





## Extras Guide

#### how to format README 

https://github.com/tchapi/markdown-cheatsheet

#### how to add images in README 

guide >> https://stackoverflow.com/questions/14494747/how-to-add-images-to-readme-md-on-github

#### how to add emoji 

https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md

https://www.webfx.com/tools/emoji-cheat-sheet/


