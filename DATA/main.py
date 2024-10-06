#tentativa 1 de criptografia

import hashlib
crypt = hashlib.md5()
crypt.update(b"hello")
print(crypt.hexdigest())
