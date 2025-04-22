#!/usr/bin/env python3
import sys
from collections import defaultdict

def read_edgelist(idxbase):
    """Reads edges from stdin and returns a list of (node1, node2) tuples."""
    edges = []
    for line in sys.stdin:
        stripped = line.strip()
        parts = stripped.split()
        if len(parts) != 2:
            raise ValueError(f"Invalid edge format: '{line.strip()}'")
        node1, node2 = parts
        edges.append((int(node1)-idxbase, int(node2)-idxbase))
    return edges

def build_adjacency_list(edges):
    """Builds an adjacency list from a list of edges."""
    adj_list = defaultdict(list)
    for u, v in edges:
        if u < v:
            adj_list[u].append(v)
        else:
            adj_list[v].append(u)
    return adj_list

def write_adjacency_list(adj_list, idxbase):
    """Writes the adjacency list to stdout."""
    for node in sorted(adj_list):
        neighbors = " ".join(map(lambda x: str(x+idxbase), sorted(adj_list[node])))
        print(f"{node+idxbase} {neighbors}")

def main():
    edges = read_edgelist(0)
    adj_list = build_adjacency_list(edges)
    write_adjacency_list(adj_list, 1)

if __name__ == "__main__":
    main()
