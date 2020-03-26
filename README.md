# Overview

This document is so that I can understand the structure behind Great Expectations is that I have to understand the structure of the code and what it does.

https://docs.greatexpectations.io/en/latest/intro.html


### Here are the list of things that Great Expectations can do, according to the Introduction.
* Save time during data cleaning and munging.
* Accelerate ETL and data normalization.
* Streamline analyst-to-engineer handoffs.
* Streamline knowledge capture and requirements gathering from subject-matter experts.
* Monitor data quality in production data pipelines and data products.
* Automate verification of new data deliveries from vendors and other teams.
* Simplify debugging data pipelines if (when) they break.
* Codify assumptions used to build models when sharing with other teams or analysts.
    - this would be very very helpful
* Develop rich, shared data documention in the course of normal work.
    - is this something that is automatically generated?
* Make implicit knowledge explicit.

### Key Features and Terms

An Expectation is something that is conceptually similar to assertions in Unittesting. Great Expectations currently supports native execution of Expectations in three environments: pandas, SQL (through the SQLAlchemy core), and Spark. This approach follows the philosophy of “take the compute to the data" (this may be where I can have the easiest contribution... implementing something that is already there in another language or context)

DataContext and DataSource
Writing pipeline tests from scratch can be tedious and counterintuitive. Great Expectations jump starts the process by providing powerful tools for automated data profiling. This provides the double benefit of helping you explore data faster, and capturing knowledge for future documentation and testing.


## Medium Articles
There are 3 Medium articles pro

 


## Tutorial
The initial installation of the package is simple enough, with a ```pip install great_expectations``` command.  The next thing they want you to do is run ```great_expectations init``` which creates a new data project. There you specifiy the language you want to use and the data that you want to import.

There is a really nice example project .git that is given by the great_expectations site. It downloads a dataset from the United States Centers for Medicare and Medicaid Services National Provider Identifier Standard (NPI).

Currently the data is arranged in this way :

```SHELL
/Users/willshin/Development/GreatExpectations_Notes/ge_example_project/data/npidata/npidata_pfile_20190902-20190908.csv
/Users/willshin/Development/GreatExpectations_Notes/ge_example_project/data/npidata/npidata_pfile_20190909-20190915.csv

```



## Overall structure

## What is the structure of the code?


## Tasks that I might be able to tackle
