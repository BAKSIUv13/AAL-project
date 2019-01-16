# unique-variables
# Bartlomiej Kulik

"""Main program module."""

# TESTS - everythin below will be removed
from algorithms import optimum
from algorithms import brute_force

TEST_STRING = 'uucuuucuucucuuucusciaxaaxaxxaxaaxaxaxxxaxaxasdbfsfhnkjsnejkfjjsdnkjcnsdkncsdkc'

UQ_VARIABLES_BRUT = brute_force.brute_force(TEST_STRING)
UQ_VARIABLES_BRUT = list(UQ_VARIABLES_BRUT)
UQ_VARIABLES_BRUT.sort()

UQ_VARIABLES_OPTIMUM = optimum.Optimum(TEST_STRING).optimum()
UQ_VARIABLES_OPTIMUM.sort()

print('is the same: ', UQ_VARIABLES_BRUT == UQ_VARIABLES_OPTIMUM)

print(len(UQ_VARIABLES_BRUT), len(UQ_VARIABLES_OPTIMUM))
