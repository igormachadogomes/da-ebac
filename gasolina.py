import pandas as pd
import seaborn as sns

data = pd.read_csv("gasolina.csv")
with sns.axes_style('whitegrid'):
 grafico = sns.lineplot(data=data, x="dia", y="venda", palette="pastel")
 grafico.set(title='Preço da gasolina por dia', xlabel='Dia', ylabel='Preço (USD)')

fig = grafico.get_figure()
fig.savefig('gasolina.png')

