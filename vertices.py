import networkx as nx
import matplotlib.pyplot as plt

# Take input from user
n = int(input("Enter the number of vertices: "))

if n > 3:
    # Create complete graph
    G = nx.complete_graph(n)


    # Draw graph
    nx.draw(
        G,
        node_color='green',
        node_size=1500,
        with_labels=True
    )

    plt.show()
else:
    print("Minimum number of vertices should be more than 3")