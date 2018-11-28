load_file_in_context('script.py')
from hashlib import sha256

test_nonce_a = 0
test_proof_a = sha256((str(new_transactions) + str(test_nonce_a)).encode()).hexdigest()
while test_proof_a[:2] != '0'*difficulty:
  test_nonce_a += 1
  test_proof_a = sha256((str(new_transactions)+str(test_nonce_a)).encode()).hexdigest()

test_nonce_b = 0
test_proof_b = sha256((str(test_nonce_b) + str(new_transactions)).encode()).hexdigest()
while test_proof_b[:2] != '0'*difficulty:
  test_nonce_b += 1
  test_proof_b = sha256((str(test_nonce_b) + str(new_transactions)).encode()).hexdigest()

import re
with open('script.py','r') as file:
  if re.search('(final_proof)', file.read()):
    if final_proof[:2] == '00':
      if final_proof == test_proof_a or final_proof == test_proof_b:
        pass_tests()
      elif final_proof != test_proof_a and final_proof != test_proof_b:
        fail_tests('Proof has leading zeros but has the wrong value')
    elif final_proof[:2] != '00':
      fail_tests("Proof doesn't have two leading zeros")
  else:
    fail_tests("Did you remember to define 'final_proof'?")