import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "uVF1VcSb8HY35NsUBGfTyhFAeyyjrmxk"

while True:
   orig = str(input("Ingrese punto de partida: "))
   if orig == "quit" or orig == "q":
        break
   dest = str(input("Ingrese destino: "))
   if dest == "quit" or dest == "q":
        break
   print("==============================================")
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")

    print("=============================================")
    print("Viaje de " + (orig) + " hasta " + (dest))
    print("Duracion del viaje: " + (json_data["route"]["formattedTime"]))
    print("Kilometros: " + str("{:.2f}".format(json_data["route"]["distance"]*1.61)))
    print("=============================================")
    print("=============Narrativa del viaje=============")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
    print("=============================================\n")

    print("Para salir del programa Sdel viaje escribir #quit# o presionar la letra #q#")

    print("=============================================")
    print("=============================================")
