import math
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.cost_matrix = [[0] * num_nodes for _ in range(num_nodes)]
        self.node_dict = {}

    def print_matrix(self):
        for fila in self.cost_matrix :
            for j in fila:
                print(j, end=" ")
            print()

    def add_node(self, node_id, node):
        self.node_dict[node_id] = node

    def add_edge(self, src_id, dest_id):
        if src_id != dest_id:
            src_node = self.node_dict[src_id]
            dest_node = self.node_dict[dest_id]
            weight = self.calculate_distance(src_node.coordinates, dest_node.coordinates)
            self.cost_matrix[src_id][dest_id] = weight
            self.cost_matrix[dest_id][src_id] = weight

    def calculate_distance(self, coordinates1, coordinates2):
        x1, y1 = coordinates1
        x2, y2 = coordinates2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def plot_graph(self):
        fig, ax = plt.subplots()
        nodes = list(self.node_dict.values())
        coordinates = [node.coordinates for node in nodes]
        demands = [node.demand for node in nodes]

        # ax.scatter(*zip(*coordinates), s=demands, color='red')
        for i, (x, y) in enumerate(coordinates):
            label = chr(ord('A') + i)  # Etiqueta letras mayúsculas: A, B, C, ...
            ax.scatter(x, y, s=demands[i] * 0.05, color='red')
            ax.annotate(label, (x, y), textcoords="offset points", xytext=(0,10), ha='center')


        ax.set_aspect('equal')

        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                if self.cost_matrix[i][j] != 0:
                    ax.plot([coordinates[i][0], coordinates[j][0]], [coordinates[i][1], coordinates[j][1]], color='black')

        # ax.set_xlim(65, 75)
        # ax.set_ylim(15, 45)

        ax.set_xlim(0, 25)
        ax.set_ylim(0, 25)

        plt.show()

    def plot_graph_with_path(self, path):
        fig, ax = plt.subplots()
        nodes = list(self.node_dict.values())
        coordinates = [node.coordinates for node in nodes]
        demands = [node.demand for node in nodes]

        ax.scatter(*zip(*coordinates), s=[demand * 0.05 for demand in demands], color='red')
        ax.set_aspect('equal')

        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                if self.cost_matrix[i][j] != 0:
                    if i in path and j in path:
                        idx_i = path.index(i)
                        idx_j = path.index(j)
                        if idx_i < idx_j:
                            ax.plot([coordinates[i][0], coordinates[j][0]], [coordinates[i][1], coordinates[j][1]], color='blue')
                            ax.text((coordinates[i][0] + coordinates[j][0]) / 2, (coordinates[i][1] + coordinates[j][1]) / 2, str(idx_i+1), color='blue')
                        else:
                            ax.plot([coordinates[i][0], coordinates[j][0]], [coordinates[i][1], coordinates[j][1]], color='blue')
                            ax.text((coordinates[i][0] + coordinates[j][0]) / 2, (coordinates[i][1] + coordinates[j][1]) / 2, str(idx_j+1), color='blue')
                    else:
                        ax.plot([coordinates[i][0], coordinates[j][0]], [coordinates[i][1], coordinates[j][1]], color='black')

        # ax.set_xlim(65, 75)
        # ax.set_ylim(15, 45)

        def __str__ (self):
            return f"las coordenadas x son{self.coo}"
        ax.set_xlim(0, 25)
        ax.set_ylim(0, 25)

        plt.show()