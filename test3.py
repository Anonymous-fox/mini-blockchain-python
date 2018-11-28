load_file_in_context('script.py')
test_nonce = str(nonce)
test_transactions = str(new_transactions)
test_combination = test_nonce + test_transactions
test_proof = sha256(test_combination.encode()).hexdigest()

import re

with open('script.py','r') as file:
  if re.search('(proof)', file.read()):
    if proof == test_proof:
      pass_tests()
    elif proof != test_proof:
      fail_tests()
  else:
    fail_tests()