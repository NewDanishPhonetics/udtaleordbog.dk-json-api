q = "stabel"                # *required, your query
std = "ipa"                 # optional(default=ipa), supported standards: ipa, narrow, bdg, udt, ddo, ng, dania, kiel
norm = "1"                  # optional(default=1), supported norms: 1 = Standard, 2 = Conservative, 3 = Ultra conservative, 4 = Younger
api_key = "api_key"         # *required for full access, request an API key at https://udtaleordbog.dk/kontakt.php, or check your existing API_key at https://udtaleordbog.dk/profil.php

import requests
import json
url = 'https://udtaleordbog.dk/api.php'
mydata = {"q":q, "norm":norm, "std":std, "api_key":api_key}
r=requests.post(url, data=mydata).content
r = r.decode("utf-8")
r = json.loads(r)

print(r["pron"])
