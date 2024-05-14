
from argument import HIArgs, args_zips
from cca import get_cca
from uhc import get_uhc

def get_option(prompt: str, options: list) -> int:
    print(prompt)
    for i, v in enumerate(options):
        print(f'[{i+1}] {v}')
    while True:
        i = input('$ ')
        if not i.isdigit() or not len(options) > int(i)-1 or int(i)-1 < 0 or i == '':
            print('\033[31mInvalid response!\033[m')
            continue
        return int(i)-1
def get_number(prompt: str, can_be_float: bool = False) -> int|float:
    print(prompt)
    print(f'Answer must be a {"whole " if not can_be_float else ""}number')
    while True:
        i = input('$ ')
        if not i.isdigit() or i == '':
            print('\033[31mInvalid response!\033[m')
            continue
        return int(i) if not can_be_float else float(i)
def get_str(prompt: str, can_be_empty: bool = False) -> str:
    print(prompt)
    while True:
        i = input('$ ')
        if not can_be_empty and i == '' or i.isspace():
            print('\033[31mInvalid response!\033[m')
            continue
        return i

def get_family_member():
    return [
        get_number('How old is this family member?'),
        True if get_option('What gender is this family member?', ['Male', 'Female']) == 0 else False
    ]

hh_income = get_number("What is your yearly annual income?")
zip_code  = get_option("What is your zip code?", args_zips)
print('\nTime for family members.')
family = []
family.append(get_family_member())
while True:
    print()
    cont = get_option("Do you want to add another family member?", ["Yes", "No"])
    if cont == 1: break
    family.append(get_family_member())

args = HIArgs(hh_income, args_zips[zip_code], family)

cca = get_cca(args)
uhc = get_uhc(args)

print()
if cca:
    print(f'Covered California, Bronze: {cca.bronze}')
    print(f'Covered California, Silver: {cca.silver}')
else:
    print('Covered California does not cover your conditions.')
print()
if uhc:
    print(f'United Healthcare, Bronze: {uhc.bronze}')
    print(f'United Healthcare, Silver: {uhc.silver}')
    print(f'United Healthcare, Gold: {uhc.gold}')
    print(f'United Healthcare, Platinum: {uhc.platinum}')
else:
    print('United Healthcare does not cover your conditions.')

print()
print('Here are the plans you can take. If you earn more money or get sick less often, a higher-tiered plan would be best for you. The more expensive the plan, the better it is for saving up for a big injury or illness.')
print('Stay safe!')