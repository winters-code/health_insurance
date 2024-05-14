
import requests

handoffIdGatherURL = 'https://apply.coveredca.com/enrollment/enrldriver/v1/alt/anon/savehandoffdetails'
getDataURL = 'https://coveredca.com/enrollment/enrollment-shopping/v1/alt/anon/gethealthplans/{idn}'

def get_cca2(arg):

    res = requests.post(handoffIdGatherURL, headers={}, json={
        "shoppingGroupJson": {
            "county": "Santa Clara",
            "csLevel": "CS1",
            "enrollmentYear": "2024",
            "income": arg.income,
            "zipCode": arg.zip,
            "coverageStartDate": "5/20/2024",
            "maxAPTC": 0,
            "members": [
                {"age": a[0]} for _, a in enumerate(arg.family)
            ]
        }
    })
    ident = res.json()['handOffId']
    print(ident)

    data = requests.get(getDataURL.format(idn=ident), headers={
        "Content-Type": "application/json"
    })
    print(data)
    # print(data.text)

    with open('a.html', 'w') as f:
        f.write(data.text)
        f.close()
    