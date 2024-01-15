import bs4
import requests
import lxml

resultado = requests.get("https://www.escueladirecta.com/courses/")


sopa = bs4.BeautifulSoup(resultado.text, "lxml")

imagenes = sopa.select(".course-box-image")

for img in imagenes:
    img_cursos = requests.get(img['src'])
    f = open('mi_imagen.jpg', 'wb')
    f.write(img_cursos.content)
    f.close()

