class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, src, dest):
        if 0 <= src < self.num_vertices and 0 <= dest < self.num_vertices:
            self.adj_matrix[src][dest] = 1
            self.adj_matrix[dest][src] = 1
        else:
            print("Invalid vertex.")

    def remove_edge(self, src, dest):
        if 0 <= src < self.num_vertices and 0 <= dest < self.num_vertices:
            self.adj_matrix[src][dest] = 0
            self.adj_matrix[dest][src] = 0
        else:
            print("Invalid vertex.")

    def print_graph(self):
        for row in self.adj_matrix:
            print(" ".join(str(val) for val in row))


# Example usage
num_vertices = int(input("Enter the number of vertices: "))
graph = Graph(num_vertices)

while True:
    print("\nMenu:")
    print("1. Add an edge")
    print("2. Remove an edge")
    print("3. Print the graph")
    print("4. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        src = int(input("Enter the source vertex: "))
        dest = int(input("Enter the destination vertex: "))
        graph.add_edge(src, dest)
    elif choice == 2:
        src = int(input("Enter the source vertex: "))
        dest = int(input("Enter the destination vertex: "))
        graph.remove_edge(src, dest)
    elif choice == 3:
        graph.print_graph()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
