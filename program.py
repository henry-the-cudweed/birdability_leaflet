import json
import snoop
data = []

with open('data/querycopy.json','r', encoding="utf8") as jsonFile:
    data = json.load(jsonFile)

print(x)


#def main():
 #   for key in range(len(data['features'])):
  #      x = data['features'][key]["attributes"]['website']
   #     urlvar = """<a href="{}"></a>""".format(x)
    #    print(urlvar) 
     #   urldata = {"url": urlvar}    
      #  data['features'][key]['attributes'] = urldata

   
   # pass

@snoop
def main():
    for feature in data['features']:
        x = feature["attributes"]['website']
        urlvar = """<a href="{}"></a>""".format(x)
        urldata = {"url": urlvar}    
        feature['attributes']['url'] = urldata


if __name__ == '__main__':
    main()