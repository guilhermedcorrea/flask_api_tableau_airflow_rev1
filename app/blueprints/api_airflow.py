from flask import Blueprint, jsonify, make_response
import requests
import json

airflow_bp = Blueprint("airflow",__name__)



@airflow_bp("api/v1/airflow/createconnection")
def create_connection_airflow():
    
    url = "/api/v1/connections"
    payload = json.dumps({
    "connection_id": "fugiat velit qui officia ex",
    "conn_type": "ut dolor esse",
    "description": "labore",
    "host": "laborum culpa Lorem consectetur",
    "login": "do nulla non",
    "schema": "Duis veniam anim",
    "port": -17006835,
    "password": "nostrud incididunt",
    "extra": "irure cillum cupidatat"
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    def wrapper():
        return 
    return jsonify(response)
    
    
@airflow_bp("api/v1/airflow/listconnection/all")
def list_connection_airflow():
    url = "/api/v1/connections?limit=100&offset=81377175&order_by=dolor commodo amet minim in"

    payload = {}
    headers = {
    'Accept': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    def wrapper():
        return 
    return jsonify(response)


@airflow_bp("api/v1/airflow/listdag/all")
def list_dag_run():
    url = "/api/v1/dags/dolor commodo amet minim in/dagRuns?limit=100&offset=81377175&execution_date_gte=1995-04-22T15:24:08.219Z&execution_date_lte=1995-04-22T15:24:08.219Z&start_date_gte=1995-04-22T15:24:08.219Z&start_date_lte=1995-04-22T15:24:08.219Z&end_date_gte=1995-04-22T15:24:08.219Z&end_date_lte=1995-04-22T15:24:08.219Z&state=velit cupidatat tempor&state=elit in veniam&order_by=dolor commodo amet minim in"

    payload = {}
    headers = {
    'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    def wrapper():
        return 
    return jsonify(response)
    
    

@airflow_bp("api/v1/airflow/dataset/all")   
def list_data_set():
    url = "/api/v1/datasets?limit=100&offset=81377175&order_by=dolor commodo amet minim in&uri_pattern=dolor commodo amet minim in"

    payload = {}
    headers = {
    'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    def wrapper():
        return 
    return jsonify(response)
