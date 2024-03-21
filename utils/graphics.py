import matplotlib.pyplot as plt
from scipy.stats import normaltest, probplot
import seaborn as sns
import numpy as np

def show_graphics(data):
  
  # boxplot
  fig_bloxplot = plt.figure(1, (10, 7))
    
  plt.boxplot(data)
  plt.title("Gráfico Boxplot")
  plt.ylabel("Acurácia (%)")
  plt.show()
  fig_bloxplot.savefig('assets/boxplot.png', format='png')
    
  # Q-Q
  fig_q_q, ax = plt.subplots(figsize=(8, 4))
  probplot(data, plot=ax)

  plt.title("Gráfico Q-Q")
  plt.ylabel("Acurácia (%)")
  plt.xlabel("Quantis teóricos")

  plt.show()
  fig_q_q.savefig('assets/q-q.png', format='png')
    
  # Histogram
  sns.histplot(data, kde=True)
  plt.title("Gráfico Histograma")
  plt.ylabel("Frequência ")
  plt.xlabel("Acurácia (%)")
  plt.savefig("assets/histogram.png")
  plt.show() 


# Criando dados aleatórios

# Criando o gráfico de calor
  data = np.random.rand(10, 12)
  print(data)
  sns.heatmap(data)

# Adicionando título e rótulos dos eixos
  plt.title('Gráfico de Calor')
  plt.xlabel('Eixo X')
  plt.ylabel('Eixo Y')
  plt.show()





