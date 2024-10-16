#Importamos la libreria

import pandas as pd

#Escribimos los datos
fbk = ['Facebook', 2449, True, 2006]
twt = ['Twitter', 339, False, 2006]
ig = ['Instagram', 1000, True, 2010]
yt = ['Yotube', 2000, False, 2005]
lkn = ['Linkedin', 663, False,2003]
wsp = ['WhatsApp', 1600, True, 2009] 

lista_rrss = [fbk, twt, ig, yt, lkn, wsp]

#creamos dataframe a partir de la listas
df_rss=pd.DataFrame(lista_rrss, columns = ['Nombre', 'Cantidad', 'ES_FBK', 'Año'])
print(df_rss)
