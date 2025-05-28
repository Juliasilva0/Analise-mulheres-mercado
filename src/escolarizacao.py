import pandas as pd
import folium
import json
from folium.features import GeoJsonTooltip


df = pd.read_csv(r"C:\Users\julia\OneDrive\Documentos\Bigdata\src\dados_para_mapa.csv")
df['Valor'] = df['Valor'].str.replace('"', '').str.replace(',', '.').astype(float)
df.columns = df.columns.str.strip()


geojson_path = r"C:\Users\julia\OneDrive\Documentos\Bigdata\src\br_states.geojson"
with open(geojson_path, encoding='utf-8') as f:
    geojson_data = json.load(f)


mapa = folium.Map(location=[-14.2350, -51.9253], zoom_start=4, tiles='CartoDB positron')


def get_color(valor, sexo):
    if pd.isna(valor):
        return 'gray'
    if sexo == 'Mulheres':
        if valor < 5:
            return '#fde0dd'
        elif valor < 10:
            return '#fa9fb5'
        else:
            return '#c51b8a'
    elif sexo == 'Homens':
        if valor < 5:
            return '#deebf7'
        elif valor < 10:
            return '#9ecae1'
        else:
            return '#08519c'
    return 'white'


def adicionar_mapa_por_sexo(sexo):
    df_sexo = df[df['Sexo'] == sexo]
    

    geojson_atualizado = json.loads(json.dumps(geojson_data))  
    for feature in geojson_atualizado['features']:
        estado = feature['properties']['name']
        valor = df_sexo.loc[df_sexo['Local'] == estado, 'Valor']
        if not valor.empty:
            feature['properties']['Valor'] = round(valor.values[0], 2)
        else:
            feature['properties']['Valor'] = None

    
    grupo = folium.FeatureGroup(name=f'{sexo}')

    folium.GeoJson(
        geojson_atualizado,
        style_function=lambda feature: {
            'fillColor': get_color(feature['properties']['Valor'], sexo),
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.7,
        },
        tooltip=GeoJsonTooltip(
            fields=["name", "Valor"],
            aliases=["Estado:", "Escolarização (%):"],
            localize=True,
            sticky=False,
            labels=True,
            style=(
                "background-color: white; color: #333333; font-family: Arial; "
                "font-size: 12px; padding: 5px;"
            )
        )
    ).add_to(grupo)

    grupo.add_to(mapa)

adicionar_mapa_por_sexo('Mulheres')
adicionar_mapa_por_sexo('Homens')


folium.LayerControl(collapsed=False).add_to(mapa)

mapa.save(r"C:\Users\julia\OneDrive\Documentos\Bigdata\src\mapa_por_sexo.html")
