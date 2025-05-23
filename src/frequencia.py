import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\julia\OneDrive\Documentos\Bigdata\src\dados_escolares.csv")
print(df.head())

df_total_brasil = df[(df['CorOuRaca'] == 'Total') & (df['Região'] == 'Brasil')]

df_total_brasil['Diferença_Mulher_Homem'] = df_total_brasil['Mulher'] - df_total_brasil['Homem']

print(df_total_brasil[['Ano', 'Homem', 'Mulher', 'Diferença_Mulher_Homem']])

plt.figure(figsize=(10,6))


plt.plot(df_total_brasil['Ano'], df_total_brasil['Homem'], marker='o', label='Homens', color='blue')
plt.plot(df_total_brasil['Ano'], df_total_brasil['Mulher'], marker='o', label='Mulheres', color='purple')


plt.fill_between(df_total_brasil['Ano'],
                 df_total_brasil['Homem'],
                 df_total_brasil['Mulher'],
                 color='violet', alpha=0.3)

plt.title('Frequência Escolar de Crianças de 5 anos - Brasil')
plt.xlabel('Ano')
plt.ylabel('Frequência Escolar (%)')
plt.legend()
plt.grid(True)


plt.savefig('frequencia_genero_5anos.png', dpi=300)
plt.show()
