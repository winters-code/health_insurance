
from argument import HIArgs, args_zips
from cca import get_cca
from uhc import get_uhc
# from cca2 import get_cca2

# get_cca2(test_args)

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

# hh_income = get_number("What is your yearly annual income?")
# zip_code  = get_option("What is your zip code?", args_zips)
# family = []
# family.append(get_family_member())
# while True:
#     cont = get_option("Do you want to add another family member?", ["Yes", "No"])
#     if cont == 1: break
#     family.append(get_family_member())

args = HIArgs(100000, 94040, [(10, True), (40, False)])

print('Covered California')
print(repr(get_cca(args)))
print('United Healthcare')
print(repr(get_uhc(args)))