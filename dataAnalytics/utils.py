import matplotlib.pyplot as plt
import base64
from io import BytesIO
import pandas as pd


def fill_nan(df):
    numeric = ['float64', 'int64']
    for i in range(len(df.columns)):
        x = df.iloc[:, i]
        if x.dtype in numeric:
            x.fillna(value=x.mean(), inplace=True)
        else:
            x.fillna(value=x.value_counts().index[0], inplace=True)


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(df,x_label, y_label):
    x = df[x_label]
    y = df[y_label]
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title(x_label + " vs " + y_label)
    plt.plot(x, y)
    plt.xticks(rotation=45)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.tight_layout()
    graph = get_graph()
    return graph
