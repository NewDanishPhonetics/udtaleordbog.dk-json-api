q = "stabel"                # *required, query
std = "ipa"                 # optional(default=ipa), supported standards: ipa, narrow, bdg, udt, ddo, ng, dania, kiel
norm = "1"                  # optional(default=1), supported norms: 1 = Standard, 2 = Conservative, 3 = Ultra conservative, 4 = Younger
email = "your@mail.com"     # *required for full access, your login email for udtaleordbog.dk, signup at https://udtaleordbog.dk/signup.php
password = "yourpassword"   # *required for full access, your password for udtaleordbog.dk, signup at https://udtaleordbog.dk/signup.php

import requests
import json
url = 'https://udtaleordbog.dk/api.php'
mydata = {"q":q, "norm":norm, "std":std, "email":email, "password":password}
r=requests.post(url, data=mydata).content
r = r.decode("utf-8")
r = json.loads(r)

print(r["pron"])
