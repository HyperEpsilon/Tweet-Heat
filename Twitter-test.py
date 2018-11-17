import twitter

api = twitter.Api(consumer_key=['9DylZjpQIUOuRDVev7BRlShUS'],
                  consumer_secret=['WvDaTcYz3c70xgsadKBdi9BrfjpQEiymiOrPsg2KNVnZppnQo6'],
                  access_token_key=['1063915931066261504-FwDnh5XsrB0Hb0dVzsbfW0omgyMrKS'],
                  access_token_secret=['BrNAzfPwQGzb1rAuJCBC2EiC6HvFEXpVFBh9AZEWrpoTy'])

statuses = api.GetUserTimeline(1063915931066261504)
print([s.text for s in statuses])