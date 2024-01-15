import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")
# print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')

# print(sopa.select('title'))
# TRAE UN ARRAY CON LOS ELEMENTOS CON DICHA ETIQUETA

# print(sopa.select('title')[0])
# TRAE SIN []

# print(sopa.select('title')[0].getText())
# OBTIENE EN TEXTO

parrafo_especial = sopa.select('p')
# print(parrafo_especial[3].getText())

# EXTRAER CLASE COMPLETA

# # ELEMENTO QUE CONTENGA ID
# . ELEMENTOS QUE CONTENGAN CLASE
# autor = sopa.select(".author-name")

# "div span" CUALQUIER ELEMENTO SPAN QUE ESTE DENTRO DE UN DIV
barra_lateral = sopa.select(".PopularPosts div.widget-content h3")

for e in barra_lateral:
    print(e.getText())


# > "div>span" CUALQUIER ELEMENTO SPAN QUE ESTE DENTRO DE UN DIV, SIN NINGUN ELEMENTO DE POR MEDIO