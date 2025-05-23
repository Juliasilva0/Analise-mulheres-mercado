import plotly.graph_objects as go
import pandas as pd

# Carregar e tratar os dados
df = pd.read_csv(r"C:\Users\julia\OneDrive\Documentos\Bigdata\src\dados_atividades.csv")

# Corrigir os nomes das colunas
df.rename(columns=lambda x: x.strip(), inplace=True)

# Limpeza dos dados — transformar em float
df['Homem'] = df['Homem'].astype(str).str.replace(' ', '').str.replace(',', '.').astype(float)
df['Mulher'] = df['Mulher'].astype(str).str.replace(' ', '').str.replace(',', '.').astype(float)

# Agrupar os dados por Ano (média salarial)
df_ano = df.groupby('Ano').agg({'Homem': 'mean', 'Mulher': 'mean'}).reset_index()

# Criar o gráfico
fig = go.Figure()

fig.add_trace(go.Bar(
    x=df_ano['Ano'],
    y=df_ano['Homem'],
    name='Homem',
    marker_color='#1f77b4',
    text=df_ano['Homem'].round(2),
    textposition='outside'
))

fig.add_trace(go.Bar(
    x=df_ano['Ano'],
    y=df_ano['Mulher'],
    name='Mulher',
    marker_color='#800080',
    text=df_ano['Mulher'].round(2),
    textposition='outside'
))

# Personalizar o layout
fig.update_layout(
    title='<b>Salário Médio por Ano e Gênero</b>',
    xaxis_title='Ano',
    yaxis_title='Salário Médio (R$)',
    barmode='group',
    template='plotly_white',
    legend=dict(
        title='Gênero',
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    font=dict(
        family="Arial",
        size=14
    )
)

# Exportar como HTML para usar no site
fig.write_html("grafico_salario_interativo.html")

