class BayesianNetwork:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.cpts = {}

    def add_node(self, node, parents, cpt):
        self.nodes[node] = cpt
        self.edges[node] = parents

    def get_parents(self, node):
        return self.edges[node]

    def get_cpt(self, node):
        return self.nodes[node]

def enumerate_all(vars, evidences, network):
    if not vars:
        return 1.0
    first, *rest = vars
    parents = tuple(evidences[parent] for parent in network.get_parents(first))
    if first in evidences:
        prob = network.get_cpt(first)[parents][evidences[first]]
        return prob * enumerate_all(rest, evidences, network)
    else:
        total = 0
        for val in [True, False]:
            new_evidences = evidences.copy()
            new_evidences[first] = val
            prob = network.get_cpt(first)[parents][val]
            total += prob * enumerate_all(rest, new_evidences, network)
        return total

def query(variables, evidence, network):
    normalized = {}
    evidences = evidence.copy()
    for var in variables:
        normalized[var] = {}
        for val in [True, False]:
            evidences[var] = val
            normalized[var][val] = enumerate_all(list(network.nodes.keys()), evidences, network)
        total = sum(normalized[var].values())
        for val in normalized[var]:
            normalized[var][val] /= total
    return normalized



# Conditional Probability Tables (CPT)
rain_cpt = {(): {True: 0.2, False: 0.8}}

sprinkler_cpt = {
    (True,): {True: 0.01, False: 0.99},
    (False,): {True: 0.4, False: 0.6}
}

wet_grass_cpt = {
    (True, True): {True: 0.99, False: 0.01},
    (True, False): {True: 0.8, False: 0.2},
    (False, True): {True: 0.9, False: 0.1},
    (False, False): {True: 0.0, False: 1.0}
}

network = BayesianNetwork()
network.add_node("Rain", [], rain_cpt)
network.add_node("Sprinkler", ["Rain"], sprinkler_cpt)
network.add_node("WetGrass", ["Rain", "Sprinkler"], wet_grass_cpt)


# Query the probability of Rain given that the Grass is Wet
result = query(["Rain"], {"WetGrass": True}, network)
print(result)
