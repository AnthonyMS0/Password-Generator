import random
import time
import string

caracteres = string.ascii_letters + string.punctuation + string.digits
pss = "".join(random.choice(caracteres)for x in range (random.randint(8,16)))
print("Loading...")
time.sleep(3)
print(pss)

