import bs4
import requests

url_base = "https://books.toscrape.com/catalogue/page-{}.html"

libro_rating_alto = []

for pagina in range(1, 5):
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)

    sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')
    libros = sopa.select('.product_pod')

    for libro in libros:
        # CHEQUEAR ESTRELLAS
        ejemplo = libro.select('.star-rating.Four') or libro.select('.star-rating.Five')
        # Si es igual a 0 quiere decir que no tiene las estrellas necesarias
        if ejemplo:
            # OBTENGO TITULO
            titulo_libro = libro.select("a")[1]['title']
            libro_rating_alto.append(titulo_libro)


for libro in libro_rating_alto:
    print(f"Libro: {libro}")