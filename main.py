
from argument import HIArgs
from cca import get_cca
from uhc import get_uhc

test_args = HIArgs(10000, 94040, [(40, True), (38, False)])

print('Covered California')
print(repr(get_cca(test_args)))
print('United Healthcare')
print(repr(get_uhc(test_args)))