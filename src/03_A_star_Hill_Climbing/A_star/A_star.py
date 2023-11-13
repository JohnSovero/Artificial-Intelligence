from collections import deque
 
class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
 
    def get_neighbors(self, v):
        return self.adjac_lis[v]
 
    def h(self, n):
        H = {
            'A': 10,
            'B': 8,
            'C': 5,
            'D': 7,
            'E': 3,
            'F': 6,
            'G': 5,
            'H': 3,
            'I': 1,
            'J': 0,
        }
 
        return H[n]
 
    def a_star_algorithm(self, start, stop):
        open_lst = set([start])
        closed_lst = set([])

        poo = {}
        poo[start] = 0

        par = {}
        par[start] = start
 
        while len(open_lst) > 0:
            n = None

            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v;
 
            if n == None:
                print('Ruta no existe!')
                return None

            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                print('Ruta encontrada (nodos): {}'.format(reconst_path))
                return reconst_path
 
            for (m, weight) in self.get_neighbors(n):
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Esta ruta no existe')
        return None


""" adjac_lis = {
    'A': [('B', 3), ('C', 4), ('F', 7)],
    'B': [('A', 3), ('H',6)],
    'C': [('A', 4), ('H',3), ('D',5)],
    'D': [('H',2), ('C',5), ('F',7),('G',2),('I',12)],
    'E': [('F',4), ('I',6)],
    'F': [('A',7), ('D',7),('I',16),('E',4)],
    'G': [('H',1), ('I',5),('D',2)],
    'H': [('B',6),('C',3),('D',2),('G',1)],
    'I': [('E',6),('F',16),('D',12),('G',5)]
} """
adjac_lis = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C',3)],
    'C': [('B', 3), ('D',1), ('E',5)],
    'D': [('C',1), ('E',8)],
    'E': [('C',5), ('D',8), ('J',5), ('I',5)],
    'F': [('A',3), ('G',1),('H',7)],
    'G': [('F',1), ('I',3)],
    'H': [('F',7),('I',2)],
    'I': [('E',5),('G',3),('J',3), ('H',2)]
}
grafo = Graph(adjac_lis)
grafo.a_star_algorithm('A', 'J')