import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, Canvas, Scrollbar, Text
from PIL import Image, ImageTk

class GraphVisualizer:
    def __init__(self):
        self.G = nx.Graph()
        self.node_colors = {}
        self.edge_colors = {}

        self.window = tk.Tk()
        self.window.title("VisuaLearn || Graph Traversal Algorithms")
        self.window.geometry("1100x950")
        self.window.resizable(width=False, height=False)

        self.canvas = Canvas(self.window, width=1100, height=950)
        self.canvas.pack(fill="both", expand=True)
        self.apply_gradient_background()

        # Title
        self.title_label = tk.Label(self.window, text="Graph Visualizer", font=("Arial", 30, "bold"), bg="#cf5808", fg="black", borderwidth=2, relief="ridge")
        self.title_label.place(x=350, y=15)

        # Add Node
        self.node_label = tk.Label(self.window, text="Enter Node:", font=("Arial", 20, "bold"), bg="yellow", fg="black")
        self.node_label.place(x=20, y=100)

        self.node_entry = tk.Entry(self.window, font=("Arial", 20), bd=2)
        self.node_entry.place(x=440, y=100)

        self.add_node_button = tk.Button(self.window, text="Add Node", command=self.add_node, font=("Arial", 20, "bold"), bg="lightblue")
        self.add_node_button.place(x=800, y=100)

        # Node List Display
        self.node_list_label = tk.Label(self.window, text="Nodes Added:", font=("Arial", 16, "bold"), bg="lightgray")
        self.node_list_label.place(x=20, y=190)

        self.node_list_text = Text(self.window, height=3, width=50, font=("Arial", 14))
        self.node_list_text.place(x=20, y=220)

        # Add Edge
        self.edge_label = tk.Label(self.window, text="Enter Edge (node1 node2):", font=("Arial", 20, "bold"), bg="yellow", fg="black")
        self.edge_label.place(x=20, y=360)

        self.edge_entry = tk.Entry(self.window, font=("Arial", 20), bd=2)
        self.edge_entry.place(x=440, y=360)

        self.add_edge_button = tk.Button(self.window, text="Add Edge", command=self.add_edge, font=("Arial", 20, "bold"), bg="lightgreen")
        self.add_edge_button.place(x=800, y=360)

        # Edge List Display
        self.edge_list_label = tk.Label(self.window, text="Edges Added:", font=("Arial", 16, "bold"), bg="lightgray")
        self.edge_list_label.place(x=20, y=410)

        self.edge_list_text = Text(self.window, height=3, width=50, font=("Arial", 14))
        self.edge_list_text.place(x=20, y=440)

        # Start Node for DFS/BFS
        self.start_node_label = tk.Label(self.window, text="Enter Start Node for DFS/BFS:", font=("Arial", 20, "bold"), bg="yellow", fg="black")
        self.start_node_label.place(x=20, y=560)

        self.start_node_entry = tk.Entry(self.window, font=("Arial", 20), bd=2)
        self.start_node_entry.place(x=440, y=560)

        self.dfs_button = tk.Button(self.window, text="DFS", command=self.dfs, font=("Arial", 20, "bold"), bg="lightcoral")
        self.dfs_button.place(x=800, y=560)

        self.bfs_button = tk.Button(self.window, text="BFS", command=self.bfs, font=("Arial", 20, "bold"), bg="lightyellow")
        self.bfs_button.place(x=900, y=560)

        self.visualize_button = tk.Button(self.window, text="Visualize Graph", command=self.visualize, font=("Arial", 20, "bold"), bg="lightgray")
        self.visualize_button.place(x=280, y=640)

        self.clear_button = tk.Button(self.window, text="Clear Graph", command=self.clear_graph, font=("Arial", 20, "bold"), bg="tomato")
        self.clear_button.place(x=520, y=640)

        # Display Result
        self.result_label = tk.Label(self.window, text="Traversal Result:", font=("Arial", 20, "bold"), bg="#dec962", fg="black")
        self.result_label.place(x=20, y=720)

        self.result_text = Text(self.window, height=5, width=60, font=("Arial", 16))
        self.result_text.place(x=20, y=760)

    def apply_gradient_background(self):
        for i in range(950):
            r = max(0, min(255, int(255 - (i / 600) * 150)))
            g = max(0, min(255, int(100 + (i / 600) * 100)))
            b = max(0, min(255, int(200 - (i / 600) * 50)))
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas.create_line(0, i, 1100, i, fill=color)

    def add_node(self):
        node = self.node_entry.get().split(",")
        if node:
            for i in node:
                self.G.add_node(i)
                self.node_colors[i] = 'lightblue'
                self.node_entry.delete(0, tk.END)
                self.update_node_list()
        else:
            messagebox.showerror("Input Error", "Please enter a valid node name.")

    def add_edge(self):
        edge = self.edge_entry.get().split()
        if len(edge) == 2 and all(node in self.G for node in edge):
            self.G.add_edge(edge[0], edge[1])
            self.edge_colors[(edge[0], edge[1])] = 'gray'
            self.edge_entry.delete(0, tk.END)
            self.update_edge_list()
        else:
            messagebox.showerror("Input Error", "Please enter a valid edge with existing nodes.")

    def update_node_list(self):
        self.node_list_text.delete(1.0, tk.END)
        self.node_list_text.insert(tk.END, ", ".join(self.G.nodes()))

    def update_edge_list(self):
        self.edge_list_text.delete(1.0, tk.END)
        self.edge_list_text.insert(tk.END, ", ".join(f"{u}-{v}" for u, v in self.G.edges()))

    def dfs(self):
        start_node = self.start_node_entry.get()
        if start_node not in self.G.nodes():
            messagebox.showerror("Error", "Start node does not exist!")
            return
        self.reset_graph_colors()
        visited = set()
        traversal_order = []

        if start_node not in visited:
            self._dfs_helper(start_node, visited, traversal_order)

        for node in self.G.nodes():
            if node not in visited:
                self._dfs_helper(node, visited, traversal_order)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "DFS Traversal Order: " + str(traversal_order))

    def _dfs_helper(self, node, visited, traversal_order):
        visited.add(node)
        traversal_order.append(node)
        self.node_colors[node] = 'red'
        self.update_visualization()
        for neighbor in self.G.neighbors(node):
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited, traversal_order)

    def bfs(self):
        start_node = self.start_node_entry.get()
        if start_node not in self.G.nodes():
            messagebox.showerror("Error", "Start node does not exist!")
            return
        self.reset_graph_colors()
        visited = set()
        traversal_order = []
        queue = []

        if start_node not in visited:
            queue.append(start_node)
            visited.add(start_node)

            while queue:
                node = queue.pop(0)
                traversal_order.append(node)
                self.node_colors[node] = 'red'
                self.update_visualization()
                for neighbor in self.G.neighbors(node):
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

        for other_node in self.G.nodes():
            if other_node not in visited:
                queue.append(other_node)
                visited.add(other_node)
                while queue:
                    node = queue.pop(0)
                    traversal_order.append(node)
                    self.node_colors[node] = 'red'
                    self.update_visualization()
                    for neighbor in self.G.neighbors(node):
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "BFS Traversal Order: " + str(traversal_order))

    def reset_graph_colors(self):
        for node in self.G.nodes():
            self.node_colors[node] = 'lightblue'
        for edge in self.G.edges():
            self.edge_colors[edge] = 'gray'

    def update_visualization(self):
        plt.clf()
        pos = nx.spring_layout(self.G, seed=42)
        node_colors = [self.node_colors[node] for node in self.G.nodes()]
        edge_colors = [self.edge_colors.get(edge, 'gray') for edge in self.G.edges()]
        nx.draw(self.G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, width=2, node_size=1000, font_size=12, font_weight="bold")
        plt.draw()
        plt.pause(1)

    def visualize(self):
        plt.clf()
        pos = nx.spring_layout(self.G, seed=42)
        node_colors = [self.node_colors[node] for node in self.G.nodes()]
        edge_colors = [self.edge_colors.get(edge, 'gray') for edge in self.G.edges()]
        nx.draw(self.G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, width=2, node_size=1000, font_size=12, font_weight="bold")
        plt.show()

    def clear_graph(self):
        self.G.clear()
        self.node_colors.clear()
        self.edge_colors.clear()
        self.result_text.delete(1.0, tk.END)
        self.node_list_text.delete(1.0, tk.END)
        self.edge_list_text.delete(1.0, tk.END)
        self.visualize()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    visualizer = GraphVisualizer()
    visualizer.run()
