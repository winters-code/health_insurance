
"""
Health Insurance Calculator
------------------------------------
Code by: Weston

This file is for getting the data from Covered California.
Make sure you have 'argument.py' in the same directory!
"""

import requests, json, datetime
from argument import HIRes

today = datetime.datetime.now(datetime.timezone.utc).today()
tomorrow = today + datetime.timedelta(days=1)

payload = {
    'isChildAlone': 'false',
    'paymentModes[]': 'M',
    'applicationType': '',
    'isWindowShopping': 'false',
    'currentDate': today.strftime('%Y-%m-%d'),
    #'currentDate': '2024-04-25',
    'quoteSource': 'UHC Store - DTC',
    'applicationSource': 'UHC Store',
    'effectiveDate': tomorrow.strftime('%Y-%m-%d'),
    #'effectiveDate': '2024-04-26',
    'vueBrokerId': '',
    'userType': 'CONSUMER',
    'localeCode': 'en-US',
    'zipCode': '94040', # We will assume the person is living in Santa Clara.
    'county': 'SANTA CLARA', # Zip code really should not have an impact as long as the county is the same.
    'countyFipsCode': '06085',
    'state': 'CA'
}
url = 'https://www.uhc.com/shop/api/products'
header = {
    'Accept':'application/json',
    'Referer':'https://www.uhc.com/shop/individuals-families/en/quote/plans/hospitalindemnity?leadsourcename=UHC-IandF&tfn=1-800-557-6718',
    'Request-Id':'|c9b18f1cc96146db93078b1327cbd0d0.99f5cd9e84e14c7a',
    'Requestguid':'D5B210A7-2D5B-E511-80D1-005056BD5356',
    'Sec-Ch-Ua':'"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':"macOS",
    'Traceparent':'00-c9b18f1cc96146db93078b1327cbd0d0-99f5cd9e84e14c7a-01',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

def get_uhc(args):
    for i, f in enumerate(args.family):
        payload[f'applicants[{i}].applicantTypeCode'] = 'P'
        payload[f'applicants[{i}].gender'] = 'M' if f[1] else 'F'
        payload[f'applicants[{i}].isTobacco'] = False
        payload[f'applicants[{i}].birthDate'] = args.get_dob(i)
        payload[f'applicants[{i}].healthClassName'] = 'Preferred'

    res = requests.get(url, params=payload, headers=header)
    data = res.json()

    with open('a.json', 'w') as f:
        f.write(json.dumps(data))
        f.close()

    resu = HIRes()
    resu.bronze = data[0]["planRates"][0]["rateAmount"]
    resu.silver = data[1]["planRates"][0]["rateAmount"]
    resu.gold = data[-2]["planRates"][0]["rateAmount"]
    resu.platinum = data[-1]["planRates"][0]["rateAmount"]

    return resu

    
