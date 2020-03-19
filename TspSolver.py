from AdjMatReader import *


# Tsp solver with forward and recursive method (+memoization) C(s, i) = min(C(s-{i}, j_ + dist(j, i)) if |S| > 2 else dist(start_node, i)
class TspSolver(AdjMatReader):
    def __init__(self, csv_dir, start_node):
        AdjMatReader.__init__(self, csv_dir)  # object which contains adjacency matrix and node list
        self.start_node = str(start_node)  # starting node
        self.cost_dict = {}  # dictionary for C(S, i) - memoization
        self.cost_interm_node_dict = {}  # dictionary for j which minimizes the C(S, i) - memoization

    def get_key(self, node_set, dest):  # get key for cost_dict & cost_interm_node_dict dictionary
        return str(np.array(node_set)) + str(dest)

    def dist(self, src, dest):  # distance from src node to dest node - get value from adjacency matrix
        return self.adj_matrix[np.where(self.node_list == src)[0][0], np.where(self.node_list == dest)[0][0]]

    def cost(self, node_set, dest):  # cost function - C(S, i)
        cost_key = self.get_key(node_set, dest)  # get key whether to find reusable data or store data
        if cost_key in self.cost_dict.keys():  # return cost if it is already in the dictionary
            return self.cost_dict[cost_key]

        if len(node_set) == 1:  # rather than finding |S| == 2, I choose to find |S| == 1 case which denotes S = {i}, so we could consider S as {start_node, i}
            self.cost_dict[cost_key] = self.dist(self.start_node, node_set[0])
            self.cost_interm_node_dict[cost_key] = [self.start_node, node_set[0]]
            return self.cost_dict[cost_key]

        elif len(node_set) > 1:
            interm_candidate_node_set = [node for node in node_set if node != dest and node != self.start_node]  # node list which can be intermediate node for minimum cost path - j

            min_cost = np.inf  # set minimum as infinity
            min_cost_node = None  # node which minimizes the cost - j* --> j* is optimal j
            node_set_wo_dest = [node for node in node_set if node != dest]  # S-{i}
            for interm_candidate_node in interm_candidate_node_set:
                cost_candidate = self.cost(node_set_wo_dest, interm_candidate_node) + self.dist(interm_candidate_node, dest)  # C(S-{i}, j) + dist(j, i)
                if cost_candidate < min_cost:  # save minimum cost and optimal j
                    min_cost = cost_candidate
                    min_cost_node = interm_candidate_node

            # save to the dictionary
            self.cost_dict[cost_key] = min_cost
            self.cost_interm_node_dict[cost_key] = [*self.cost_interm_node_dict[self.get_key(node_set_wo_dest, min_cost_node)], dest]
            return self.cost_dict[cost_key]
        else:
            raise AttributeError("Unable to solve")

    def solve(self):
        return self.cost(self.node_list, self.start_node), self.cost_interm_node_dict[self.get_key(self.node_list, self.start_node)]


if __name__ == "__main__":
    solver = TspSolver('./adj_matrix4.csv', 1)
    print(solver.solve())
