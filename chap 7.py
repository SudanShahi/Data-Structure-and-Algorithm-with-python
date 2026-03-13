"""
class MachineNetwork:
    def __init__(self):
        self.machine_links = {}

    def add_machine(self, machine):
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, m1, m2):
        if m1 not in self.machine_links:
            self.add_machine(m1)
        if m2 not in self.machine_links:
            self.add_machine(m2)

        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)
        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    def print_network(self):
        for machine, connections in self.machine_links.items():
            print(f"{machine}: {connections}")

    def print_connected_machines(self, machine):
        if machine in self.machine_links:
            print(f"{machine} is connected to: {self.machine_links[machine]}")
        else:
            print(f"{machine} not found in network")

# Create the network
network = MachineNetwork()

# Add links as specified
network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

# Test Exercise 1
print("Exercise 1: Print Network")
network.print_network()
print("\nConnected machines:")
network.print_connected_machines("Machine_C")

Exercie 2.
class MachineNetwork:
    def __init__(self):
        self.machine_links = {}

    def add_machine(self, machine):
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, m1, m2):
        if m1 not in self.machine_links:
            self.add_machine(m1)
        if m2 not in self.machine_links:
            self.add_machine(m2)

        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)
        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    def print_network(self):
        for machine, connections in self.machine_links.items():
            print(f"{machine}: {connections}")

    def print_connected_machines(self, machine):
        if machine in self.machine_links:
            print(f"{machine} is connected to: {self.machine_links[machine]}")
        else:
            print(f"{machine} not found in network")

    def bfs(self, start):
        if start not in self.machine_links:
            print(f"Error: {start} does not exist")
            return []

        visited = []
        queue = [start]

        while queue:
            machine = queue.pop(0)
            if machine not in visited:
                visited.append(machine)
                for neighbor in self.machine_links[machine]:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)

        return visited

# Create the network
network = MachineNetwork()

# Add links as specified
network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

# Test Exercise 2
print("Exercise 2: BFS")
print(network.bfs("Machine_A"))

Exercie 3.
class MachineNetwork:
    def __init__(self):
        self.machine_links = {}

    def add_machine(self, machine):
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, m1, m2):
        if m1 not in self.machine_links:
            self.add_machine(m1)
        if m2 not in self.machine_links:
            self.add_machine(m2)

        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)
        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    def print_network(self):
        for machine, connections in self.machine_links.items():
            print(f"{machine}: {connections}")

    def print_connected_machines(self, machine):
        if machine in self.machine_links:
            print(f"{machine} is connected to: {self.machine_links[machine]}")
        else:
            print(f"{machine} not found in network")

    def dfs(self, start):
        if start not in self.machine_links:
            print(f"Error: {start} does not exist")
            return []

        visited = []
        stack = [start]

        while stack:
            machine = stack.pop()
            if machine not in visited:
                visited.append(machine)
                for neighbor in self.machine_links[machine]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return visited

# Create the network
network = MachineNetwork()

# Add links as specified
network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

# Test Exercise 3
print("Exercise 3: DFS")
print(network.dfs("Machine_A"))
"""