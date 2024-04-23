# api_script.py

import sys
from infermedica_api import InfermedicaApi

def fetch_conditions():
    api = InfermedicaApi(app_id='your_app_id', app_key='your_app_key')
    # Code to fetch conditions using API
    return conditions

if __name__ == "__main__":
    conditions = fetch_conditions()
    with open('api_output.txt', 'w') as f:
        for condition in conditions:
            f.write(f"{condition.common_name}: {condition.probability}% probability\n")
    print("API data saved to api_output.txt")
