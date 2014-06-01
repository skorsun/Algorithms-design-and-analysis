__author__ = 'bell'

from math import log, ceil
from random import randint


class Vertex(object):
    def __init__(self, _id, _edges):
        self.id = _id
        self.edges = _edges


class Edge(object):
    def __init__(self, _vertices):
        self.vertices = _vertices


def min_cut(id2vertex, edges):
    while len(id2vertex.keys()) > 2:
        randedge = edges[randint(0, len(edges) - 1)]
        first = randedge.vertices[0]
        second = randedge.vertices[1]
        # always merge second to first
        remove = []
        for i, e in enumerate(first.edges):
            for v in e.vertices:
                if second.id == v.id:
                    remove.append(i)
        for r in remove[::-1]:
            del first.edges[r]
        remove = []
        for i, e in enumerate(second.edges):
            for v in e.vertices:
                if first.id == v.id:
                    remove.append(i)
        for r in remove[::-1]:
            del second.edges[r]
        remove = []
        for i, e in enumerate(edges):
            if (e.vertices[0].id == first.id and e.vertices[1].id == second.id) or \
                    (e.vertices[1].id == first.id and e.vertices[0].id == second.id):
                remove.append(i)
        for r in remove[::-1]:
            del edges[r]
        for e in second.edges:
            replace = None
            for i, v in enumerate(e.vertices):
                if v.id == second.id:
                    replace = i
            del e.vertices[replace]
            e.vertices.append(first)
        first.edges = first.edges + second.edges
        del id2vertex[second.id]

    return len(edges)


lines = None


def init():
    global lines

    if lines is None:
        import os
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        lines = [line for line in open(os.path.join(__location__, 'kargerMinCut.txt'))]

    id2vertex = {}
    edges = []
    for line in lines:
        parts = line.strip().split('\t')
        id_ = parts[0]
        connected_vertices = parts[1:]
        if id_ in id2vertex:
            vertex = id2vertex[id_]
        else:
            vertex = id2vertex[id_] = Vertex(id_, [])
        for conn_id in connected_vertices:
            if conn_id in id2vertex:
                conn_v = id2vertex[conn_id]
                get_out = False
                for e in conn_v.edges:
                    for v in e.vertices:
                        if id_ == v.id:
                            get_out = True
                            break
                    if get_out:
                        break
                if get_out:
                    continue
            else:
                conn_v = Vertex(conn_id, [])
                id2vertex[conn_id] = conn_v
            new_edge = Edge([vertex, conn_v])
            vertex.edges.append(new_edge)
            conn_v.edges.append(new_edge)
            edges.append(new_edge)

    return id2vertex, edges


if __name__ == '__main__':


    from sys import maxsize
    m = maxsize

    from util.timeit import timeit

    @timeit
    def run():
        """
            current runtime:
                    10  iterations  -        1.625   sec
                   100  iterations  -       15.58    sec
                  1000  iterations  -      155.8     sec    ~   3 min
                 10000  iterations  -     1558       sec    ~  30 min
                100000  iterations  -    15580       sec    ~ 300 min
                200000  iterations  -    31160       sec    ~ 600 min ~ 10 hours


        """
        global m
        for r in range(int(ceil(200*200*log(200)))):
            res = min_cut(*init())
            if res < m:
                m = res

    try:
        run()
    finally:
        print m  # 17
