names = ["usa", "poland", "uzbekistan", "tanzania"]
pop = [318968000, 38485779, 30185000, 47400000]
language = ["english", "polish", "uzbek", "swahili"]
gdp = ["$53,001", "$21,118","$4,038","$1,813"]
capital = ["Washington, D.C.", "Warsaw", "Tashkent", "Dar es Salaam"]

countries = {}
for i in range(0, len(names)):
    countries[names[i]] = {
        "population": pop[i],
        "majority language": language[i],
        "GDP per cap": gdp[i],
        "capital": capital[i]
}

countries.items()