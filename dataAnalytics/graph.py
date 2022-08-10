import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64
import seaborn as sns


def covert_graph_to_image():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


class Colors:
    RED, GREEN, BLUE, ORANGE = 'r', 'g', 'b', 'o'


class Graph:
    SIZE = (10, 5)

    def __init__(self, df, *args):
        self.data = df
        self.cols = args
        self.colTypes = []
        for i in args:
            if df[i].dtype in ['int64', 'float64']:
                self.colTypes.append(1)
            else:
                self.colTypes.append(0)
        # self.colTypes = [1 if df[i].dtype in ['int64','float64'] else 0 for i in args]

    def get_suitable_plots(self):
        if len(self.cols) !=2:
            return None
        else:
            graphs = []
            if self.colTypes.count(1) == len(self.cols):
                graphs.extend([self.get_line_plot(), self.get_bar_plot(),
                               self.get_scatter_plot(), self.get_multi_area_plot()])
                return graphs
            elif self.colTypes.count(0) == len(self.cols):
                return None
            else:
                graphs.extend([self.get_line_plot(), self.get_bar_plot(),
                               self.get_scatter_plot(), self.get_pie_plot()])
                return graphs

    def get_line_plot(self):
        data = self.cols
        x = self.data[data[0]]
        y = self.data[data[1]]
        plt.switch_backend('AGG')
        plt.figure(figsize=Graph.SIZE)
        plt.title(data[0] + " vs " + data[1])
        plt.plot(x, y)
        plt.xticks(rotation=45)
        plt.xlabel(data[0])
        plt.ylabel(data[1])
        plt.tight_layout()
        graph = covert_graph_to_image()
        return graph

    def get_bar_plot(self):
        data = self.cols
        x = self.data[data[0]]
        y = self.data[data[1]]
        plt.switch_backend('AGG')
        plt.figure(figsize=Graph.SIZE)
        plt.title(data[0] + " vs " + data[1])
        plt.bar(x, y)
        plt.xticks(rotation=45)
        plt.xlabel(data[0])
        plt.ylabel(data[1])
        plt.tight_layout()
        graph = covert_graph_to_image()
        return graph

    def get_scatter_plot(self):
        data = self.cols
        x = self.data[data[0]]
        y = self.data[data[1]]
        plt.switch_backend('AGG')
        plt.figure(figsize=Graph.SIZE)
        plt.title(data[0] + " vs " + data[1])
        plt.scatter(x, y)
        plt.xticks(rotation=45)
        plt.xlabel(data[0])
        plt.ylabel(data[1])
        plt.tight_layout()
        graph = covert_graph_to_image()
        return graph

    def get_single_area_plot(self):
        data = self.cols
        x = self.data[data[0]]
        sns.set(style="darkgrid")
        plt.switch_backend('AGG')
        plt.figure(figsize=Graph.SIZE)
        plt.title(data[0] + " area plot")
        plt.xticks(rotation=45)
        plt.xlabel(data[0])
        plt.ylabel(data[0])
        plt.tight_layout()
        sns.kdeplot(x, shade=True)
        graph = covert_graph_to_image()
        return graph

    def get_multi_area_plot(self):
        data = self.cols
        x = self.data[data[0]]
        y = self.data[data[1]]
        sns.set(style="darkgrid")
        plt.switch_backend('AGG')
        plt.figure(figsize=Graph.SIZE)
        plt.title(f"Area plot between {data[0]} and {data[1]}")
        plt.xticks(rotation=45)
        plt.xlabel(data[0])
        plt.ylabel(data[1])
        plt.tight_layout()
        sns.kdeplot(x, shade=True, color=Colors.RED)
        sns.kdeplot(y, shade=True, color=Colors.GREEN)
        graph = covert_graph_to_image()
        return graph

    def get_pie_plot(self):
        data = self.cols
        sns.set(style="darkgrid")
        plt.switch_backend('AGG')
        plt.figure(figsize=Graph.SIZE)
        d = dict(self.data.groupby([data[1]])[data[0]].sum())
        plt.pie(d.values())
        plt.legend(labels=d.keys())
        plt.title(f"Area plot between {data[0]} and {data[1]}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        graph = covert_graph_to_image()
        return graph

    def get_pair_plot(self):
        #TODO: pair plot for multiple columns
        pass
