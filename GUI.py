import tkinter as tk
import math
import random
import heapq

# Initialize variables
start_node = None
end_node = None
nodes = {}  # Dictionary to store node positions
edges = []  # List to store edges (represented as tuples of node positions)
edges_weights = {}  # Dictionary to store edge weights

def create_node(event):
    global start_node
    # Create a node at the clicked position
    x, y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
    start_node = (x, y)

def draw_line(event):
    global start_node
    if start_node:
        # Draw a line from start node to current mouse position
        x, y = event.x, event.y
        canvas.delete("line")
        canvas.create_line(start_node[0], start_node[1],
                            x, y, fill="black", width=2, tags="line")

def release(event):
    global start_node, end_node
    if start_node:
        # Check if released position is close to an existing node
        x, y = event.x, event.y
        for node_pos in nodes.values():
            if math.sqrt((x - node_pos[0]) ** 2 + (y - node_pos[1]) ** 2) <= 10:
                # Check if released position is close to an existing node with a line
                for edge in edges:
                    start_edge, end_edge = edge
                    start_edge_x, start_edge_y = start_edge
                    end_edge_x, end_edge_y = end_edge
                    # Check if released position is close to the start or end node of the edge
                    if math.sqrt((x - start_edge_x) ** 2 + (y - start_edge_y) ** 2) <= 10:
                        # Create a line from released position to the start node of the edge
                        canvas.create_line(x, y, start_edge_x, start_edge_y, fill="black", width=2)
                        # Store edge to the list of edges
                        edges.append(((x, y), start_edge))
                        # Reset start node
                        start_node = None
                        return
                    elif math.sqrt((x - end_edge_x) ** 2 + (y - end_edge_y) ** 2) <= 10:
                        # Create a line from released position to the end node of the edge
                        canvas.create_line(x, y, end_edge_x, end_edge_y, fill="black", width=2)
                        # Store edge to the list of edges
                        edges.append(((x, y), end_edge))
                        # Reset start node
                        start_node = None
                        return

        # If released position is not close to an existing node, create a node at the released position
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
        end_node = (x, y)

        # Draw a line between start node and end node
        canvas.delete("line")
        canvas.create_line(start_node[0], start_node[1],
                            end_node[0], end_node[1],
                            fill="black", width=2)

        # Store node position
        nodes[start_node] = end_node

        # Calculate distance between nodes (Euclidean distance)
        distance = math.sqrt((start_node[0] - end_node[0]) ** 2 +
                                (start_node[1] - end_node[1]) ** 2)

        # Random weight for the edge
        weight = random.randint(1, 10)

        # Store edge weight in a dictionary
        edges_weights[(start_node, end_node)] = weight

        # Print edge and weight
        print(f"Edge: {start_node} - {end_node}, Weight: {weight}")

        # Reset start node
        start_node = None


def prim_algorithm():
    pass

def kruskal_algorithm():
    pass

# Function to clear canvas
def clear_canvas():
    canvas.delete("all")
    global nodes, edges, edges_weights
    nodes = {}
    edges = []
    edges_weights = {}

# Create the Tkinter window
root = tk.Tk()
root.title("Minimum Spanning Tree")

# Create a canvas widget
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Create buttons
prim_button = tk.Button(root, text="Prim's Algorithm", command=prim_algorithm)
prim_button.pack(side="left", padx=10, pady=10)

kruskal_button = tk.Button(root, text="Kruskal's Algorithm", command=kruskal_algorithm)
kruskal_button.pack(side="left", padx=10, pady=10)

clear_button = tk.Button(root, text="Clear Canvas", command=clear_canvas)
clear_button.pack(side="left", padx=10, pady=10)

# Bind mouse events
canvas.bind("<Button-1>", create_node)
canvas.bind("<B1-Motion>", draw_line)
canvas.bind("<ButtonRelease-1>", release)

# Run the Tkinter event loop
root.mainloop()

