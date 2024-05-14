"""
Health Insurance Calculator
------------------------------------
Code by: Weston

This file is for getting the data from Covered California.
Make sure you have 'argument.py' in the same directory!
"""

import requests, json
from argument import HIRes

payload = {
    "formValues": {
        "coverageYear": "2024",
        "zip": "94039",
        "county": "Santa Clara",
        "householdSize": "1",
        "householdIncome": "100000",
        "householdMembers": [
            21
        ],
        "didReceiveUnemploymentInsurance": False
    }
}
url = "https://coveredcalifornia-calculator-api.azurewebsites.net/api/subsidy-calculator/calculate"
header = {
    "Content-Type": "application/json",
    "Priority": "u=1, i",
    "Origin": "https://www.coveredca.com"
}

def get_cca(args):
    payload["formValues"]["zip"] = args.zip
    payload["formValues"]["county"] = args.county
    payload["formValues"]["householdSize"] = len(args.family)
    payload["formValues"]["householdMembers"] = list(map(lambda x: x[0], args.family))
    payload["formValues"]["householdIncome"] = args.income

    res = requests.post(url, headers=header, json=payload)

    if res.status_code != 200:
        return None
    
    data = res.json()
    
    result = HIRes(
        bronze = float(data.get('lowestBronzeRate', None)),
        silver = float(data.get('secondLowestSilverRate', None))
    )
    return result
