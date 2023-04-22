from flask import Blueprint



import requests

def add_surce_scheduler():
    
    url = "https://{{server}}/api/{{api-version}}/sites/{{site-id}}/schedules/{{schedule-id}}/datasources"

    payload = "<tsRequest>\n  <task>\n    <extractRefresh>\n      <datasource id=\"{{datasource-id}}\" />\n    </extractRefresh>\n  </task>\n</tsRequest>"
    headers = {
    'Content-Type': 'application/xml',
    'X-Tableau-Auth': ''
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)
    
    
def add_workbook_to_schedule():
    url = "https://{{server}}/api/{{api-version}}/sites/{{site-id}}/schedules/{{schedule-id}}/workbooks"

    payload = "<tsRequest>\n  <task>\n    <extractRefresh>\n      <workbook id=\"{{workbook-id}}\" />\n    </extractRefresh>\n    <!-- If taskType is dataAcceleration change body to below> -->\n    <dataAcceleration>\n      <workbook id=\"{{workbook-id}}\" />\n    </dataAcceleration>\n  </task>\n</tsRequest>\n"
    headers = {
    'Content-Type': 'application/xml',
    'X-Tableau-Auth': ''
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)
    
    

def cancela_job():
    url = "https://{{server}}/api/{{api-version}}/sites/{{site-id}}/jobs/{{job-id}}"

    payload = {}
    headers = {
    'X-Tableau-Auth': ''
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)
    
    
def get_extract_refresh_tasks():
    url = "https://{{server}}/api/{{api-version}}/sites/{{site-id}}/schedules/{{schedule-id}}/extracts"

    payload = {}
    headers = {
    'X-Tableau-Auth': ''
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    
def get_schedule():
    url = "https://{{server}}/api/{{api-version}}/schedules"

    payload = {}
    headers = {
    'X-Tableau-Auth': ''
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    
    
def update_Schedule():
    url = "https://{{server}}/api/{{api-version}}/schedules/{{schedule-id}}"

    payload = "<tsResponse>\n  <schedule id=\"{{schedule-id}}\"\n        name=\"schedule-name\"\n        state=\"new-state\"\n        priority=\"schedule-priority\"\n        createdAt=\"datetime-created\"\n        updatedAt=\"datetime-updated\"\n        type=\"Extract-or-Subscription\"\n        frequency=\"schedule-frequency\"\n        nextRunAt=\"datetime-next-run\"\n        endScheduleAt =\"datetime-expiration\"\n        executionOrder=\"Parallel-or-Serial\">\n        <frequencyDetails frequency-expression >\n            <intervals>\n               <interval interval-expression />\n             </intervals>\n        </frequencyDetails>\n  </schedule>\n</tsResponse>"
    headers = {
    'Content-Type': 'application/xml',
    'X-Tableau-Auth': ''
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)
