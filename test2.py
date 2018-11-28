load_file_in_context('script.py')
test_proof_a = sha256((str(nonce) + str(new_transactions)).encode()).hexdigest()
test_proof_b = sha256((str(new_transactions) + str(nonce)).encode()).hexdigest()

import re

with open('script.py','r') as file:
  if re.search('(proof)', file.read()):
    if proof == test_proof_a or proof == test_proof_b:
      pass_tests()
    elif proof != test_proof_a and proof != test_proof_b:
      fail_tests("Proof found was not correct")
  else:
    fail_tests("Did you remember to define the variable 'proof' ?")