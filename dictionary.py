#dict={"who":"Rick Astley", 1: "FAIL"}
#print(dict[1])
#print(dict["who"])
#dict["candy"] = "chocolate"
#print(dict["candy"])
#print(dict)
#dict["candy"] = "gummy"
#for key in dict.keys():
    #print(key)
d1 = {"Kabul":"Afghanistan","Tirana":"Albania", "Algiers":"Algeria", "Andorra la Vella":"Andorra","Luanda":"Angola",
      "Saint John's":"Antigua and Barbuda","Buenos Aires":"Argentina","Yerevan":"Armenia","Canberra":"Australia",
      "Vienna":"Austria","Baku":"Azerbaijan","Nassau":"Bahamas","Manama":"Bahrain","Dhaka":"Bangladesh",
      "Barbados":"Bridgetown","Minsk":"Belarus","Brussels":"Belgium","Belmopan":"Belize","Porto-Novo":"Benin",
      "Thimphu":"Bhutan","Sucre":"Bolivia","Sarajevo":"Bosnia and Herzegovina","Gaborone":"Botswana",
      "Brasilia":"Brazil","Bandar Seri Begawan":"Brunei","Sofia":"Bulgaria","Ouagadougou":"Burkina Faso",
      "Gitega":"Burundi","Yamoussoukro": "Cote d'Ivoire", }
for key in d1:
    print(f"{key}:{d1[key]}")