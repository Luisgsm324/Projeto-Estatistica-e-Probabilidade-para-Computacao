
from utils.central_measures import central_measures
from utils.graphics import show_graphics



def remove_linebreak_transform_float(value):
  value = value.replace("/n", "")
  value = float(value)
  return value

data = open("data/data_7.csv", mode="r" ,encoding="utf8" )
data = map(remove_linebreak_transform_float, data)
data = list(data)

central_measures(data)
show_graphics(data)

