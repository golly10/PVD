from matplotlib.pyplot import title
"""
Este script descarga los datos de consumo de energía de la ciudad de Tetouan, el cual se puede encontrar aquí https://archive.ics.uci.edu/ml/datasets/Power+consumption+of+Tetouan+city

Para crear un ejemplo de uso de plotly, se ha escogido mostrar el nivel de consumo de las tres distintas zonas registradas a lo largo del tiempo. El uso de plotly nos permite crear una gráfica interactiva
en la que se puede apreciar, haciendo zoom, los distintos intervalos de 10 segundos entre muestras y poder así, hacer una comparativa visual entre el nivel de consumo que realizan las tres zonas.

"""
import pandas as pd

import plotly.express as px


if __name__ == "__main__":

    data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00616/Tetuan%20City%20power%20consumption.csv')

    print("Datos descargados")

    fig = px.line(data, x="DateTime", y=["Zone 1 Power Consumption", "Zone 2  Power Consumption", "Zone 3  Power Consumption"], title="Power consumption")

    fig.show()