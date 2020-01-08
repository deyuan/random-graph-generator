#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Random Graph Generator

Generate various random graphs using networkx and output as edge list
Can be used as input of graph algorithm exercises

Output Format:
    5 5     # The first line contains total number of nodes and edges
    0 1     # Each of remaining lines contains from node and to node as an edge
    ...

Example:
    $ python gen_graph.py --help
    $ python gen_graph.py -grnm -n 5 -m 5
    $ python gen_graph.py -grnm -n 5 -m 5 --dir
    $ python gen_graph.py -grnm -n 5 -m 5 --one
    $ python gen_graph.py -grnm -n 5 -m 5 --vis
    $ python gen_graph.py -grnm -n 5 -m 5 --out g.txt

Author: Deyuan Guo <guodeyuan@gmail.com>
Date: Jan 5, 2020
Ref: https://networkx.github.io/documentation/stable/reference/generators.html
"""

import sys
import os
import argparse
import warnings
import networkx as nx
warnings.filterwarnings('ignore')

def int_non_neg(arg):
    """ argparse type function: a non-negative int """
    try:
        val = int(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("invalid int value: '%s'" % arg)
    if val < 0:
        raise argparse.ArgumentTypeError("must be zero or positive: '%s'" % arg)
    return val

def float_prob(arg):
    """ argparse type function: a float in range [0.0, 1.0] """
    try:
        val = float(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("invalid float value: '%s'" % arg)
    if val < 0.0 or val > 1.0:
        raise argparse.ArgumentTypeError("must be in range [0.0, 1.0]: '%s'" % arg)
    return val

def create_parser():
    """ Create argparse parser """
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help', action='help', help='show this help message and exit')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-grnm', action='store_true',
                       help='random graph with n nodes and m edges')
    group.add_argument('-grnd', action='store_true',
                       help='random graph with n nodes and d degree of each node')
    group.add_argument('-grnp', action='store_true',
                       help='random graph with n nodes and p edge creation probability')
    group.add_argument('-gkn', action='store_true',
                       help='complete graph of n nodes')
    group.add_argument('-gcn', action='store_true',
                       help='cycle graph of n cyclically connected nodes')
    group.add_argument('-gpn', action='store_true',
                       help='path graph of n linearly connected nodes')
    group.add_argument('-trn', action='store_true',
                       help='random tree with n nodes')
    group.add_argument('-tch', action='store_true',
                       help='full c-ary tree with h height')
    group.add_argument('-tcn', action='store_true',
                       help='full c-ary tree with n nodes')

    parser.add_argument('-n', metavar='node', type=int_non_neg,
                        help='number of nodes')
    parser.add_argument('-m', metavar='edge', type=int_non_neg,
                        help='number of edges')
    parser.add_argument('-d', metavar='degree', type=int_non_neg,
                        help='degree of nodes in a graph')
    parser.add_argument('-p', metavar='probability', type=float_prob,
                        help='edge creation probability')
    parser.add_argument('-h', metavar='height', type=int_non_neg,
                        help='tree height')
    parser.add_argument('-c', metavar='children', type=int_non_neg,
                        help='number of children in a tree')

    parser.add_argument('--directed', action='store_true',
                        help='generate directed graph')
    parser.add_argument('--one-based', action='store_true',
                        help='output edges using one-based node ids')
    parser.add_argument('--seed', metavar='N', type=int,
                        help='random seed')
    parser.add_argument('--visualize', action='store_true',
                        help='visualize generated graph using pyplot')
    parser.add_argument('--output', metavar='FILE', type=str,
                        help='output generated graph as an edge list to a file')

    return parser

def parse_arguments(argv):
    """ Parse command line arguments """
    parser = create_parser()
    args = parser.parse_args(argv)

    if args.n is None and not args.tch:
        parser.error('-n is required')
    if args.m is None and args.grnm:
        parser.error('-m is required')
    if args.d is None and args.grnd:
        parser.error('-d is required')
    if args.p is None and args.grnp:
        parser.error('-p is required')
    if args.h is None and args.tch:
        parser.error('-h is required')
    if args.c is None and (args.tch or args.tcn):
        parser.error('-c is required')

    if args.directed and (args.grnd or args.trn):
        parser.error('--directed is not supported for the graph type')
    if args.output is not None and os.path.exists(args.output):
        parser.error('file %s already exists' % args.output)

    return args

def gen_graph(args):
    """ Generate a graph based on command line arguments """
    graph = None
    ref = nx.DiGraph if args.directed else None
    try:
        if args.grnm:
            graph = nx.gnm_random_graph(args.n, args.m, seed=args.seed, directed=args.directed)
        elif args.grnd:
            graph = nx.random_regular_graph(args.d, args.n, seed=args.seed)
        elif args.grnp:
            graph = nx.gnp_random_graph(args.n, args.p, seed=args.seed, directed=args.directed)
        elif args.gkn:
            graph = nx.complete_graph(args.n, create_using=ref)
        elif args.gcn:
            if args.n == 0:
                raise nx.NetworkXError("n must be positive")
            graph = nx.cycle_graph(args.n, create_using=ref)
        elif args.gpn:
            graph = nx.path_graph(args.n, create_using=ref)
        elif args.trn:
            graph = nx.random_tree(args.n, seed=args.seed)
        elif args.tch:
            graph = nx.balanced_tree(args.c, args.h, create_using=ref)
        elif args.tcn:
            graph = nx.full_rary_tree(args.c, args.n, create_using=ref)
    except nx.NetworkXError as err:
        print('Error: %s' % err)
    except nx.NetworkXPointlessConcept as err:
        print('Error: %s' % err)
    return graph

def show_graph(graph):
    """ Visualize the graph """
    import matplotlib.pyplot as plt
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos=pos, with_labels=True)
    plt.show()

def output_edge_list(graph, one_based, filename):
    """ Output num node, num edge and edge list """
    num_node = graph.number_of_nodes()
    num_edge = graph.number_of_edges()
    base = 1 if one_based else 0
    edge_list = [[edge[0] + base, edge[1] + base] for edge in graph.edges()]

    if filename is None:
        print(num_node, num_edge)
        for edge in edge_list:
            print(edge[0], edge[1])
        return
    with open(filename, 'w') as fout:
        print(num_node, num_edge, file=fout)
        for edge in edge_list:
            print(edge[0], edge[1], file=fout)
    print('Saved edge list in %s' % filename)

def main(argv):
    """ Graph generator main entry """
    args = parse_arguments(argv)
    graph = gen_graph(args)
    if graph is not None:
        output_edge_list(graph, args.one_based, args.output)
        if args.visualize:
            show_graph(graph)

if __name__ == '__main__':
    main(sys.argv[1:])
