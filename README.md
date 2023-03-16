# udtaleordbog.dk-json-api

Udtaleordbog.dk's features a JSON API.

Please note, you need a personal API key to use the API. API keys are available for patrons at https://www.patreon.com/NewDanishPhonetics/ upon request. 

Without an API key, you can still access words starting with 's' in order to test applications.

The API is currently intended for personal use. There is a personal monthly limit of 1,000 requests. Contact me is you need to change the limit.

# Usage

The API can be accessed at:

	https://udtaleordbog.dk/api.php

It currently has the following structure (more data will be added in the future):

	{"ortho": "eksempel","pron": "/ɛk.ˈsɛm̰p.l/"}

You need to POST the following variables:

	'q' (Your query)
	'api_key' (Your personal API key) 

The following variables are optional:

	'std' (Your preferred phonetic notation standard, default=ipa) 
	Supported standards: ipa, narrow, bdg, udt, ddo, ng, dania, kiel

	'norm' (The desired pronunciation norm, default=1)
	Supported norms: 1 = Standard, 2 = Conservative, 3 = Ultra conservative, 4 = Younger

# Example

Refer to the python script example.
