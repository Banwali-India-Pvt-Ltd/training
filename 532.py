domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary",
    "us": "United States", "no": "Norway"  }

key = "sk"

if key in domains:
    print("{0} is in the dictionary".format(domains[key]))