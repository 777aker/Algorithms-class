"""
@author: Rhoenigman
         Shivendra
"""
import networkx as nx

"""
The function to generate the input graph

:return: Returns the NetworkX Graph for Q2
"""
def Question2():
    # Create a directed graph
    G = nx.DiGraph()

    # The 'length' on each edge should be ignored and is only for drawing.
    # Adding an edge also adds the node
    G.add_edge('EC', 'A', length=40, weight=1.0)
    G.add_edge('EC', 'H', length=40, weight=1.0)
    G.add_edge('EC', 'J', length=60, weight=1.0)

    G.add_edge('H', 'G', length=40, weight=1.0)
    G.add_edge('H', 'K', length=40, weight=1.0)

    G.add_edge('G', 'L', length=40, weight=1.0)
    G.add_edge('G', 'F', length=40, weight=1.0)

    G.add_edge('F', 'E', length=40, weight=1.0)

    G.add_edge('E', 'HUMN', length=40, weight=1.0)

    G.add_edge('J', 'S', length=80, weight=1.0)
    G.add_edge('J', 'K', length=60, weight=1.0)

    G.add_edge('K', 'L', length=40, weight=1.0)
    G.add_edge('L', 'M', length=40, weight=1.0)
    G.add_edge('M', 'N', length=40, weight=1.0)
    G.add_edge('M', 'F', length=60, weight=1.0)

    G.add_edge('N', 'O', length=80, weight=1.0)
    G.add_edge('N', 'E', length=80, weight=1.0)

    G.add_edge('O', 'HUMN', length=40, weight=1.0)

    G.add_edge('A', 'S', length=60, weight=1.0)
    G.add_edge('A', 'B', length=40, weight=1.0)

    G.add_edge('B', 'R', length=40, weight=1.0)
    G.add_edge('B', 'C', length=40, weight=1.0)

    G.add_edge('S', 'R', length=60, weight=1.0)
    G.add_edge('R', 'Q', length=40, weight=1.0)

    G.add_edge('Q', 'C', length=40, weight=1.0)
    G.add_edge('Q', 'P', length=60, weight=1.0)

    G.add_edge('C', 'D', length=40, weight=1.0)
    G.add_edge('D', 'HUMN', length=40, weight=1.0)
    G.add_edge('P', 'D', length=40, weight=1.0)
    G.add_edge('P', 'O', length=60, weight=1.0)
    G.add_edge('O', 'HUMN', length=40, weight=1.0)

    G.add_edge('T', 'Q', length=40, weight=1.0)
    G.add_edge('T', 'P', length=40, weight=1.0)
    G.add_edge('T', 'O', length=40, weight=1.0)
    G.add_edge('T', 'N', length=40, weight=1.0)
    G.add_edge('T', 'M', length=40, weight=1.0)

    G.add_edge('R', 'T', length=40, weight=1.0)
    G.add_edge('S', 'T', length=40, weight=1.0)
    G.add_edge('J', 'T', length=40, weight=1.0)
    G.add_edge('K', 'T', length=40, weight=1.0)
    G.add_edge('L', 'T', length=40, weight=1.0)

    return G


"""
A utility function to help visualize the generated graph

:param G: NetworkX Graph
:return: None (instead saves the input graph in .png format)
"""
def draw_graph(G):
    import matplotlib.pyplot as plt
    import pylab
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    node_labels = {node: node for node in G.nodes()}

    pos = nx.spectral_layout(G)
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, pos, node_size=500, edge_cmap=plt.cm.Reds)
    plt.savefig('Finals_Q2_Graph.png')
    plt.title("Input Graph")
    plt.show()



def main():
    ################## READ CAREFULLY ##############################

    # Note that you cannot use any networkx functionality
    # which makes the solution trivial

    # The 'length' on each edge (while generating the graph)
    # should be ignored and is only for drawing.
    # You should consider the 'weight' for finding the smallest path.
    # The above example has weights 1 but the weight can be anything.
    # Later on we may post some more graphs for testing.
    G = Question2()
    draw_graph(G)

    # Call your function here that takes in the Graph "G"
    # and returns the shortest path
    # (note that it is not the length but the entire path)

    # call some test cases on G
    for k in range(2, 10):
        shortestkstoppath(G, k)

def shortestkstoppath(G, k):
    # this will be a modified belman ford that instead
    # only considers exactly the number of edges

    # get the list of nodes
    nodes = G.nodes()
    # construct the table
    # the first key in the dict represents the node you are at
    # the second key in the dict represents the number of edges
    # the value represents the path length
    table = {}
    for i in nodes:
        for j in range(k+2):
            table[i, j] = -1

    # base case
    table['EC', 0] = 0

    # so this will iterate from 0 to k+2, we want k+2 because
    # the table starts from 0 and the stops is one less then the
    # number of edges we take so k+1 is k stops since you need
    # k + 1 edges to go to k stops
    for i in range(1, k+2):
        # for every node, ie the 'col' in our table
        for node in nodes:
            # for every node we are going to check and see if there
            # is a path from that node to the node we are at
            for path in nodes:
                # get the edge data for that node to this node
                data = G.get_edge_data(path, node)
                # if there wasnt a path then dont do anything
                if not data == None:
                    # so if our previous path worked for i-1, then
                    # we do this. If it didnt then we cant get to
                    # this node in i paths since we are adding an edge
                    if not table[path, i-1] == -1:
                        # so if this way is less then another solution we found then use this one
                        # instead because it is a shorter way. or if this entry hasnt been filled
                        # yet because we havent found a path then we just found one so fill it
                        if table[path, i-1] + data['weight'] <= table[node, i] or table[node, i] == -1:
                            table[node, i] = table[path, i-1] + data['weight']

    # so we made the table, but now we have to backtrack it so we
    # can say what path we took
    # the node we are currently at
    node = 'HUMN'
    # our solution path
    solution = []
    # we are gonna start at k+1, or the end, and work our way
    # backwards so set i to k+1
    i = k+1
    # this is just to skip excessive computations
    breakfor = False
    # so if we have a solution then do this
    if not table['HUMN', k+1] == -1:
        # so while we arent at the EC
        while not node == 'EC':
            # reset breakfor
            breakfor = False
            # so for every node
            for path in nodes:
                # if we still have to find a path
                if not breakfor:
                    # then get the path from that node to current node
                    data = G.get_edge_data(path, node)
                    # if there is a path
                    if not data == None:
                        # then if the spot we are currently at is equal to
                        # one less edge plus the weight of the path we are looking at
                        if table[node, i] == table[path, i-1] + data['weight']:
                            # then that path was a solution so append it
                            solution.append(node)
                            # set the node we are at to the new node
                            node = path
                            # decrement i because we just took a stop
                            i -= 1
                            # and we found a solution so don't do extra runtime
                            breakfor = True
    # append the EC because that is the final stop (easier to do here then in the loop)
    solution.append('EC')
    # reverse our solution so its in the correct order
    solution.reverse()
    # if our solution just has the EC then there wasnt a path
    if len(solution) == 1:
        print('No path from EC to HUMN when k =', k)
    # if there is a solution then print it
    else:
        print('Shortest path from EC to HUMN is:', solution)


if __name__ == "__main__":
    # The driver function
    main()