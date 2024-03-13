from statistics import median, mean, quantiles, variance
import matplotlib.pyplot as plt

def removeLine(value):
  value = value.replace("\n", "")
  value = float(value)
  return value

data = open("data_7.csv", mode="r", encoding="utf8")
data = map(removeLine, data)
data = list(data)

value_max = max(data)
value_min = min(data)
value_mean = mean(data)
value_median = median(data)
value_first_quartil, _, value_third_quartil = quantiles(data, n=4)
value_variance = variance(data)
value_desvio_padrao = value_variance ** 0.5

print("value_max:", value_max)
print("value_min:", value_min)
print("value_mean:", value_mean)
print("value_median:", value_median)
print("value_first_quartil:", value_first_quartil)
print("value_third_quartil:", value_third_quartil)
print("value_variance:", value_variance)
print("value_desvio_padrao:", value_desvio_padrao)

# Plotar gráfico de barras com estatísticas
stats_names = ['Máximo', 'Mínimo', 'Média', 'Mediana', 'Primeiro Quartil', 'Terceiro Quartil', 'Variância', 'Desvio Padrão']
stats_values = [value_max, value_min, value_mean, value_median, value_first_quartil, value_third_quartil, value_variance, value_desvio_padrao]

plt.figure(figsize=(10, 6))
plt.bar(stats_names, stats_values, color='skyblue')
plt.xlabel('Estatísticas')
plt.ylabel('Valores')
plt.title('Estatísticas dos Dados')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
