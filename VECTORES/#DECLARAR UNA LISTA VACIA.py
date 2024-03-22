
lista_vacia = []

lista_mas_cinco = [1, 2, 3, 4, 5, 6]

longitud_lista_vacia = len(lista_vacia)
longitud_lista_mas_cinco = len(lista_mas_cinco)

primer_elemento = lista_mas_cinco[0]
elemento_central = lista_mas_cinco[len(lista_mas_cinco) // 2]
ultimo_elemento = lista_mas_cinco[-1]

datos_personales = []
datos_personales.append("Junior") 
datos_personales.append(20)
datos_personales.append(1.99) 
datos_personales.append("Soltero") 
datos_personales.append("Calle Libano") 

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

it_companies.insert(2, "Xioami")

empresa_busqueda = "Oracle"
existe_empresa = empresa_busqueda in it_companies

it_companies.sort()

it_companies.reverse()

primer_empresa = it_companies.pop(0)


it_companies.clear()

print("Lista vacía:", lista_vacia)
print("Lista con más de 5 elementos:", lista_mas_cinco)
print("Longitud de lista vacía:", longitud_lista_vacia)
print("Longitud de lista con más de 5 elementos:", longitud_lista_mas_cinco)
print("Primer elemento de lista_mas_cinco:", primer_elemento)
print("Elemento central de lista_mas_cinco:", elemento_central)
print("Último elemento de lista_mas_cinco:", ultimo_elemento)
print("Datos personales:", datos_personales)
print("Lista de empresas de tecnología:", it_companies)
print("¿La empresa", empresa_busqueda, "existe en la lista de empresas de tecnología?:", existe_empresa)
print("Primera empresa eliminada:", primer_empresa)