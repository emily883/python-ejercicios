import requests

if __name__ == "__main__":
    url= "https://www.google.com/"

    response = requests.get(url)

if response.status_code == 200: #el status del servidor se guarda en el atributo status_code
  #  print(response.content) #acceder al contenido del servidor
    content = response.content
    
    file = open("google.html", "wb")
    file.write(content)
    file.close()
