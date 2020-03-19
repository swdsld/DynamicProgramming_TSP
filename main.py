from TspSolver import *
import argparse


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='./adj_matrix5.csv', help="path for the adjacency matrix")
    parser.add_argument('--start_node', default=1, help="starting node")
    return parser.parse_args()


if __name__ == "__main__":
    args = args()
    solver = TspSolver(args.path, args.start_node)
    minimum_cost, path = solver.solve()
    print('<TSP problem>')
    print('node_list:', solver.node_list)
    print('adjacency_matrix:\n', solver.adj_matrix)
    print('starting_node:', solver.start_node)
    print('\n<Answer>')
    print('cost:', minimum_cost)
    print('path:', path)
