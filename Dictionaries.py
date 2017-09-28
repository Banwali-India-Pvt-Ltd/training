# Dictionaries
dict1 = {"HindiCodingZone":"100000",
         "HindiGamingZone":"5000",
         "HindiTechZone":"10000",
         "EnglishGamingZone":"100"}

print(dict1["HindiGamingZone"])
print(dict1.get("HindiGamingZone"))


# change
dict1 = {"HindiCodingZone":"100000",
         "HindiGamingZone":"5000",
         "HindiTechZone":"10000",
         "EnglishGamingZone":"100"}
dict1['HindiGamingZone']="10000"
print(dict1["HindiGamingZone"])

print(dict1.get("HindiGamingZone"))
print(dict1.keys())
print(dict1)
print(dict1.values())

