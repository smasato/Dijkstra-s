from pyvis.network import Network
import random


def cost(node_dict: dict):
    return sum(node_dict.values())


def solve(graph: dict[str, dict], src: str, dest: str):
    dijkstra = {}

    for src_link_node in graph[src]:
        dijkstra[src_link_node] = {src: graph[src][src_link_node]}

    next_nodes = [*dijkstra]

    while len(next_nodes) != 0:
        node = next_nodes.pop(0)
        for link_node in graph[node]:
            if link_node not in dijkstra:
                next_nodes.append(link_node)
            if link_node in dijkstra:
                if cost(dijkstra[link_node]) > cost(dijkstra[node]) + graph[node][link_node]:
                    dijkstra[link_node] = {**dijkstra[node], **{node: graph[node][link_node]}}
            else:
                dijkstra[link_node] = {**dijkstra[node], **{node: graph[node][link_node]}}

    try:
        return cost(dijkstra[dest]), list(dijkstra[dest].keys()) + [dest]
    except KeyError:
        return None


def show(graph: dict[str, dict], ans: tuple[int, list]):
    g = Network(heading=str(ans), height='700px', width='1000px')
    g.toggle_physics(False)

    for node in graph.keys():
        g.add_node(node)

    for node in graph.keys():
        for link_node in graph[node]:
            try:
                s_index = ans[1].index(node)
            except ValueError:
                s_index = None

            if s_index and (ans[1][(s_index + 1) % len(ans[1])] == link_node) or (
                    s_index == 0 and ans[1][1] == link_node):
                g.add_edge(node, link_node, value=1, title=str(graph[node][link_node]), color='red')
            else:
                g.add_edge(node, link_node, value=1, title=str(graph[node][link_node]))

    g.show('_'.join(ans[1]) + '_graph.html')


def _rand(n: int, min_cost: int, max_cost: int, min_link_num: int, max_link_num: int, g_num: int):
    value = {}

    node_num = n - 2
    if node_num < 1:
        return None

    nodes = ['S'] + [str(x) for x in range(node_num)] + ['G']

    for node in nodes:
        value[node] = {}

    for node in value.keys():
        if node == 'G':
            continue

        link_nodes = random.sample(nodes, random.randrange(min_link_num, max_link_num))

        for link_node in link_nodes:
            if (node == 'S' and link_node == 'G') or nodes.index(node) >= nodes.index(link_node):
                continue

            if link_node == 'G' and g_num > 1:
                g_num -= 1
            elif link_node == 'G' and g_num == 1:
                g_num -= 1
                nodes.remove('G')

            value[node][link_node] = random.randrange(min_cost, max_cost)

    return value


def rand(n: int, min_cost: int, max_cost: int, min_link_num: int, max_link_num: int, g_num: int):
    value = _rand(n, min_cost, max_cost, min_link_num, max_link_num, g_num)
    while (not graph_check(value)) or (not solve(value, 'S', 'G')):
        value = _rand(n, min_cost, max_cost, min_link_num, max_link_num, g_num)
    return value


def graph_check(graph: dict[str, dict]):
    # isolated vertex
    for node in graph:
        if node != 'G' and graph[node] == {}:
            return False
    return True


if __name__ == '__main__':
    graph = rand(30, 1, 10, 2, 4, 6)
    ans = solve(graph, 'S', 'G')

    show(graph, ans)
