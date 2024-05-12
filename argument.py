
counties = {
    "94039": "Santa Clara",
    "94040": "Santa Clara",
    "94041": "Santa Clara",
    "94042": "Santa Clara",
    "94043": "Santa Clara",
    "94085": "Santa Clara",
    "94303": "Santa Clara"
}

class HIArgs():
    def __init__(self, income, zip_code, family) -> None:
        self.income = income
        self.zip = zip_code
        self.family = family
        self.county = counties[str(self.zip)]
    
    def get_dob(self, i):
        return f'{2024-(self.family[i][0])}-05-10'

class HIRes():
    def __init__(self, bronze=None, silver=None, gold=None, platinum=None) -> None:
        self.bronze = bronze or 'N/A'
        self.bronze_deductible = 'N/A'
        self.bronze_copay = 'N/A'
        self.silver = silver or 'N/A'
        self.silver_deductible = 'N/A'
        self.silver_copay = 'N/A'
        self.gold = gold or 'N/A'
        self.gold_deductible = 'N/A'
        self.gold_copay = 'N/A'
        self.platinum = platinum or 'N/A'
        self.platinum_deductible = 'N/A'
        self.platinum_copay = 'N/A'
    
    def __repr__(self) -> str:
        return f"""Plan Costs:
             - Bronze: {self.bronze}, d: {self.bronze_deductible}, c: {self.bronze_copay}
             - Silver: {self.silver}, d: {self.silver_deductible}, c: {self.silver_copay}
             - Gold: {self.gold}, d: {self.gold_deductible}, c: {self.gold_copay}
             - Platinum: {self.platinum}, d: {self.platinum_deductible}, c: {self.platinum_copay}"""
