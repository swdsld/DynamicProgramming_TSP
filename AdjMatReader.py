import numpy as np
import csv

# adjacency matrix reader - store matrix and node(vertex) list
class AdjMatReader:
    def __init__(self, file_dir):
        self.file_dir = file_dir  # csv file directory
        self._read()  # read function
        super(AdjMatReader, self).__init__()

    def _read(self):
        file = open(self.file_dir, 'r')  # open file
        data = csv.reader(file)  # csv object
        data_list = []  # list for matrix
        for i, data_ in enumerate(data):
            if i == 0:
                self.node_list = np.array(data_[1:], dtype=str)  # first row has node list
            else:
                if self.node_list[i - 1] != str(data_[0]):  # if starting element is not in node list, throw error
                    raise AttributeError("node list not valid")
                data_list.append(data_[1:])  # append row

        self.adj_matrix = np.array(data_list, dtype=np.float)  # adjacency matrix


if __name__ == "__main__":
    loader = AdjMatReader('./adj_matrix4.csv')
    print(loader.adj_matrix, loader.node_list)
