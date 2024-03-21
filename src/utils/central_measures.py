from statistics import median, mean, quantiles, variance, mode
from scipy.stats import kurtosis
import matplotlib.pyplot as plt

def central_measures(data):
  value_max = max(data)
  value_min = min(data)
  value_mean = mean(data)
  value_median = median(data)
  value_first_quartil, value_median, value_third_quartil = quantiles(data, n=4)
  value_variance = variance(data)
  value_standard_deviation = value_variance ** ( 1 / 2)
  value_mode = mode(data)
  value_kurtosis = kurtosis(data)

  results = [
    ["Medidas", "Valores"],
    ["Curtose", value_kurtosis],
    ["Moda", value_mode],
    ["Máximo", value_max],
    ["Mínimo", value_min],
    ["Média", value_mean],
    ["Mediana", value_median],
    ["1° Quartil", value_first_quartil],
    ["3° Quartil", value_third_quartil],
    ["Variância", value_variance],
    ["Desvio padrão", value_standard_deviation]
  ]
  

  table = plt.table(results,cellLoc="center" , loc="center", colWidths=[0.75,0.75])
  plt.axis('off')
  table.auto_set_font_size(False)
  table.set_fontsize(12)
  table.scale(0.8, 1.8)
  plt.savefig("assets/central_measures.png")
  plt.show()
  