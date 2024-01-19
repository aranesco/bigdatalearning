#Import required libraries
import pandas as pd
import json

api_url="http://127.0.0.1:5000/data"
def get_number_of_jobs_T(technology):
    payload={"Key Skills": technology}
    response=requests.get(api_url, params=payload)
    if response.ok:
        data=response.json()
        
        number_of_jobs = len(data)
        
    return technology,number_of_jobs
  
  get_number_of_jobs_T("Python")

def get_number_of_jobs_L(location):
    payload={"Location":location}
    response=requests.get(api_url, params=payload)
    if response.ok:
        data=response.json()
        
        number_of_jobs = len(data)
    #your coe goes here
    return location,number_of_jobs

#your code goes here
get_number_of_jobs_L("Los Angeles")

#your code goes here
countries = ['Los Angeles', 'New York', 'San Francisco', 'Washington DC', 'Seattle', 'Austin', 'Detroit']

# your code goes here
!pip install openpyxl
from openpyxl import Workbook

# your code goes here
wb=Workbook()
ws=wb.active
ws.append(countries)

#your code goes here
def get_number_of_jobs_TL(technology, countries):
    number_of_jobs_list = []
    for location in countries:
        payload={"Key Skills": technology, "Location": location}
        response=requests.get(api_url, params=payload)
        if response.ok:
            data=response.json()
            number_of_jobs = len(data)
            number_of_jobs_list.append(number_of_jobs)
    return number_of_jobs_list
#     return ws.append(number_of_jobs_list)

get_number_of_jobs_TL("Python", countries)

#your code goes here
wb.save('job-postings.xlsx')

# your code goes here
technology = ['C', 'C#', 'C++', 'Java', 'JavaScript', 'Python', 'Scala', 'Oracle', 'SQL Server', 'MySQL Server', 'PostgreSQL', 'MongoDB']

def get_number_of_jobs_TL(technology, countries):
    final_list=[]
    for technology in technology:
        number_of_jobs_list=[technology]
        for location in countries:
            payload={"Key Skills": technology, "Location": location}
            response=requests.get(api_url, params=payload)
            if response.ok:
                data=response.json()
                number_of_jobs = len(data)
                number_of_jobs_list.append(number_of_jobs)

        final_list.append(number_of_jobs_list)
    return final_list

get_number_of_jobs_TL(technology, countries)

data = get_number_of_jobs_TL(technology, countries)
df_data = pd.DataFrame(data, columns=['Technology', 'Los Angeles', 'New York', 'San Francisco', 'Washington DC', 'Seattle', 'Austin', 'Detroit'])
df_data



file_name = "job-postings.xlsx"
df_data.to_excel(file_name)





