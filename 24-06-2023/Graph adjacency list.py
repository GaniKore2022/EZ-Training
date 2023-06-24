class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            del self.adj_list[vertex]
            for key in self.adj_list:
                self.adj_list[key] = [v for v in self.adj_list[key] if v != vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1] = [v for v in self.adj_list[vertex1] if v != vertex2]
            self.adj_list[vertex2] = [v for v in self.adj_list[vertex2] if v != vertex1]

    def get_neighbors(self, vertex):
        if vertex in self.adj_list:
            return self.adj_list[vertex]
        return []

    def print_graph(self):
        for vertex, neighbors in self.adj_list.items():
            print(f"Vertex {vertex}: {neighbors}")

# Example usage
graph = Graph()

while True:
    print("1. Add vertex")
    print("2. Add edge")
    print("3. Remove vertex")
    print("4. Remove edge")
    print("5. Get neighbors")
    print("6. Print graph")
    print("0. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        vertex = input("Enter vertex: ")
        graph.add_vertex(vertex)
    elif choice == 2:
        vertex1 = input("Enter vertex 1: ")
        vertex2 = input("Enter vertex 2: ")
        graph.add_edge(vertex1, vertex2)
    elif choice == 3:
        vertex = input("Enter vertex: ")
        graph.remove_vertex(vertex)
    elif choice == 4:
        vertex1 = input("Enter vertex 1: ")
        vertex2 = input("Enter vertex 2: ")
        graph.remove_edge(vertex1, vertex2)
    elif choice == 5:
        vertex = input("Enter vertex: ")
        neighbors = graph.get_neighbors(vertex)
        print(f"Neighbors of vertex {vertex}: {neighbors}")
    elif choice == 6:
        graph.print_graph()
    elif choice == 0:
        break
    else:
        print("Invalid choice. Please try again.")