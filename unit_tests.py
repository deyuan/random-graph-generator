#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Random Graph Generator Unit Tests

Author: Deyuan Guo <guodeyuan@gmail.com>
Date: Jan 6, 2020
"""

from io import StringIO
import unittest
from unittest.mock import patch
import gen_graph

class TestGrnm(unittest.TestCase):
    """ Unit tests for random graph with n nodes and m edges """
    def test_grnm_n0_m0(self):
        """ Test grnm n=0 m=0 """
        argv = ['-grnm', '-n', '0', '-m', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '0 0\n')
    def test_grnm_n0_m1(self):
        """ Test grnm n=0 m=1 """
        argv = ['-grnm', '-n', '0', '-m', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '0 0\n')
    def test_grnm_n1_m0(self):
        """ Test grnm n=1 m=0 """
        argv = ['-grnm', '-n', '1', '-m', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_grnm_n1_m1(self):
        """ Test grnm n=1 m=1 """
        argv = ['-grnm', '-n', '1', '-m', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_grnm_n2_m1(self):
        """ Test grnm n=2 m=1 """
        argv = ['-grnm', '-n', '2', '-m', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n0 1\n')
    def test_grnm_n2_m2(self):
        """ Test grnm n=2 m=2 """
        argv = ['-grnm', '-n', '2', '-m', '2']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n0 1\n')
    def test_grnm_n3_m1_seed0(self):
        """ Test grnm n=3 m=1 seed=0 """
        argv = ['-grnm', '-n', '3', '-m', '1', '--seed', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 1\n0 1\n')
    def test_grnm_n3_m1_seed1(self):
        """ Test grnm n=3 m=1 seed=1 """
        argv = ['-grnm', '-n', '3', '-m', '1', '--seed', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 1\n0 2\n')
    def test_grnm_n3_m1_seed5(self):
        """ Test grnm n=3 m=1 seed=5 """
        argv = ['-grnm', '-n', '3', '-m', '1', '--seed', '5']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 1\n1 2\n')
    def test_grnm_n0_m0_dir(self):
        """ Test grnm n=0 m=0 directed """
        argv = ['-grnm', '-n', '0', '-m', '0', '--dir']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '0 0\n')
    def test_grnm_n0_m1_dir(self):
        """ Test grnm n=0 m=1 directed """
        argv = ['-grnm', '-n', '0', '-m', '1', '--dir']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '0 0\n')
    def test_grnm_n1_m0_dir(self):
        """ Test grnm n=1 m=0 directed """
        argv = ['-grnm', '-n', '1', '-m', '0', '--dir']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_grnm_n1_m1_dir(self):
        """ Test grnm n=1 m=1 directed """
        argv = ['-grnm', '-n', '1', '-m', '1', '--dir']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_grnm_n2_m1_dir_seed0(self):
        """ Test grnm n=2 m=1 drected seed=0"""
        argv = ['-grnm', '-n', '2', '-m', '1', '--dir', '--seed', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n0 1\n')
    def test_grnm_n2_m2_dir(self):
        """ Test grnm n=2 m=2 directed """
        argv = ['-grnm', '-n', '2', '-m', '2', '--dir']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 2\n0 1\n1 0\n')
    def test_grnm_n3_m1_dir_seed0(self):
        """ Test grnm n=3 m=1 directed seed=0 """
        argv = ['-grnm', '-n', '3', '-m', '1', '--dir', '--seed', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 1\n0 1\n')
    def test_grnm_n3_m1_dir_seed1(self):
        """ Test grnm n=3 m=1 directed seed=1 """
        argv = ['-grnm', '-n', '3', '-m', '1', '--dir', '--seed', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 1\n0 2\n')
    def test_grnm_n3_m1_dir_seed5(self):
        """ Test grnm n=3 m=1 directed seed=5 """
        argv = ['-grnm', '-n', '3', '-m', '1', '--dir', '--seed', '5']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 1\n2 1\n')
    def test_grnm_n2_m1_base1(self):
        """ Test grnm n=2 m=1 base=1 """
        argv = ['-grnm', '-n', '2', '-m', '1', '--one']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n1 2\n')

class TestGrnd(unittest.TestCase):
    """ Unit tests for random graph with n nodes and d degree """
    def test_grnd_n0_d0(self):
        """ Test grnd n=0 d=0 """
        argv = ['-grnd', '-n', '0', '-d', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(),
                             'Error: the 0 <= d < n inequality must be satisfied\n')
    def test_grnd_n1_d0(self):
        """ Test grnd n=1 d=0 """
        argv = ['-grnd', '-n', '1', '-d', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_grnd_n2_d1(self):
        """ Test grnd n=2 d=1 """
        argv = ['-grnd', '-n', '2', '-d', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n0 1\n')
    def test_grnd_n2_d1_base1(self):
        """ Test grnd n=2 d=1 base=1"""
        argv = ['-grnd', '-n', '2', '-d', '1', '--one']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n1 2\n')
    def test_grnd_n3_d1(self):
        """ Test grnd n=3 d=1 """
        argv = ['-grnd', '-n', '3', '-d', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), 'Error: n * d must be even\n')
    def test_grnd_n3_d2_seed0(self):
        """ Test grnd n=3 d=2 seed=0"""
        argv = ['-grnd', '-n', '3', '-d', '2', '--seed', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 3\n1 2\n1 0\n2 0\n')
    def test_grnd_n3_d2_seed1(self):
        """ Test grnd n=3 d=2 seed=1"""
        argv = ['-grnd', '-n', '3', '-d', '2', '--seed', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 3\n0 1\n0 2\n1 2\n')

class TestGrnp(unittest.TestCase):
    """ Unit tests for random graph with n nodes and p edge creation probability """
    def test_grnp_n0_p0(self):
        """ Test grnp n=0 p=0 """
        argv = ['-grnp', '-n', '0', '-p', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '0 0\n')
    def test_grnp_n1_p1(self):
        """ Test grnp n=1 p=1 """
        argv = ['-grnp', '-n', '1', '-p', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_grnp_n2_p0(self):
        """ Test grnp n=2 p=0 """
        argv = ['-grnp', '-n', '2', '-p', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 0\n')
    def test_grnp_n2_p0p5_seed0(self):
        """ Test grnp n=2 p=0.5 seed=0 """
        argv = ['-grnp', '-n', '2', '-p', '0.5', '--seed', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 0\n')
    def test_grnp_n2_p0p5_seed1(self):
        """ Test grnp n=2 p=0.5 seed=1 """
        argv = ['-grnp', '-n', '2', '-p', '0.5', '--seed', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n0 1\n')
    def test_grnp_n2_p0p5_base1_seed1(self):
        """ Test grnp n=2 p=0.5 base=1 seed=1 """
        argv = ['-grnp', '-n', '2', '-p', '0.5', '--one', '--seed', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n1 2\n')
    def test_grnp_n2_p1(self):
        """ Test grnp n=2 p=1 """
        argv = ['-grnp', '-n', '2', '-p', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n0 1\n')
    def test_grnp_n2_p1_dir(self):
        """ Test grnp n=2 p=1 directed """
        argv = ['-grnp', '-n', '2', '-p', '1', '--dir']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 2\n0 1\n1 0\n')

class TestGkn(unittest.TestCase):
    """ Unit tests for complete graph with n nodes """
    def test_gkn_n0(self):
        """ Test gkn n=0 """
        argv = ['-gkn', '-n', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '0 0\n')
    def test_gkn_n1(self):
        """ Test gkn n=1 """
        argv = ['-gkn', '-n', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_gkn_n2(self):
        """ Test gkn n=2 """
        argv = ['-gkn', '-n', '2']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n0 1\n')
    def test_gkn_n2_dir(self):
        """ Test gkn n=2 directed """
        argv = ['-gkn', '-n', '2', '--dir']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 2\n0 1\n1 0\n')
    def test_gkn_n3_dir(self):
        """ Test gkn n=3 directed """
        argv = ['-gkn', '-n', '3', '--dir']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 6\n0 1\n0 2\n1 0\n1 2\n2 0\n2 1\n')

class TestGcn(unittest.TestCase):
    """ Unit tests for cycle graph with n nodes """
    def test_gcn_n0(self):
        """ Test gcn n=0 """
        argv = ['-gcn', '-n', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), 'Error: n must be positive\n')
    def test_gcn_n1(self):
        """ Test gcn n=1 """
        argv = ['-gcn', '-n', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 1\n0 0\n')
    def test_gcn_n1_base1(self):
        """ Test gcn n=1 base=1 """
        argv = ['-gcn', '-n', '1', '--one']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 1\n1 1\n')
    def test_gcn_n2(self):
        """ Test gcn n=2 """
        argv = ['-gcn', '-n', '2']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n0 1\n')
    def test_gcn_n2_dir(self):
        """ Test gcn n=2 directed """
        argv = ['-gcn', '-n', '2', '--dir']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 2\n0 1\n1 0\n')
    def test_gcn_n3(self):
        """ Test gcn n=3 """
        argv = ['-gcn', '-n', '3']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 3\n0 1\n0 2\n1 2\n')
    def test_gcn_n3_dir(self):
        """ Test gcn n=3 directed"""
        argv = ['-gcn', '-n', '3', '--dir']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 3\n0 1\n1 2\n2 0\n')

class TestGpn(unittest.TestCase):
    """ Unit tests for path graph with n nodes """
    def test_gpn_n0(self):
        """ Test gpn n=0 """
        argv = ['-gpn', '-n', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '0 0\n')
    def test_gpn_n1(self):
        """ Test gpn n=1 """
        argv = ['-gpn', '-n', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_gpn_n2(self):
        """ Test gpn n=2 """
        argv = ['-gpn', '-n', '2']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n0 1\n')
    def test_gpn_n3(self):
        """ Test gpn n=3 """
        argv = ['-gpn', '-n', '3']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 2\n0 1\n1 2\n')

class TestTrn(unittest.TestCase):
    """ Unit tests for random tree with n nodes """
    def test_trn_n0(self):
        """ Test trn n=0 """
        argv = ['-trn', '-n', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(),
                             'Error: the null graph is not a tree\n')
    def test_trn_n1(self):
        """ Test trn n=1 """
        argv = ['-trn', '-n', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_trn_n2(self):
        """ Test trn n=2 """
        argv = ['-trn', '-n', '2']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n0 1\n')
    def test_trn_n3_seed0(self):
        """ Test trn n=3 seed=0 """
        argv = ['-trn', '-n', '3', '--seed', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 2\n0 1\n1 2\n')
    def test_trn_n3_seed1(self):
        """ Test trn n=3 seed=1 """
        argv = ['-trn', '-n', '3', '--seed', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 2\n0 1\n0 2\n')

class TestTch(unittest.TestCase):
    """ Unit tests for full c-ary tree with h height """
    def test_tch_c0_h0(self):
        """ Test tch c=0 h=0 """
        argv = ['-tch', '-c', '0', '-h', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_tch_c0_h1(self):
        """ Test tch c=0 h=1 """
        argv = ['-tch', '-c', '0', '-h', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_tch_c0_h2(self):
        """ Test tch c=0 h=2 """
        argv = ['-tch', '-c', '0', '-h', '2']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_tch_c1_h0(self):
        """ Test tch c=1 h=0 """
        argv = ['-tch', '-c', '1', '-h', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_tch_c1_h1(self):
        """ Test tch c=1 h=1 """
        argv = ['-tch', '-c', '1', '-h', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n0 1\n')
    def test_tch_c1_h2(self):
        """ Test tch c=1 h=2 """
        argv = ['-tch', '-c', '1', '-h', '2']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 2\n0 1\n1 2\n')
    def test_tch_c2_h0(self):
        """ Test tch c=2 h=0 """
        argv = ['-tch', '-c', '2', '-h', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_tch_c2_h1(self):
        """ Test tch c=2 h=1 """
        argv = ['-tch', '-c', '2', '-h', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '3 2\n0 1\n0 2\n')
    def test_tch_c2_h2(self):
        """ Test tch c=2 h=2 """
        argv = ['-tch', '-c', '2', '-h', '2']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '7 6\n0 1\n0 2\n1 3\n1 4\n2 5\n2 6\n')

class TestTcn(unittest.TestCase):
    """ Unit tests for full c-ary tree with n nodes """
    def test_tcn_c0_n0(self):
        """ Test tcn c=0 n=0 """
        argv = ['-tcn', '-c', '0', '-n', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '0 0\n')
    def test_tcn_c0_n1(self):
        """ Test tcn c=0 n=1 """
        argv = ['-tcn', '-c', '0', '-n', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_tcn_c0_n2(self):
        """ Test tcn c=0 n=2 """
        argv = ['-tcn', '-c', '0', '-n', '2']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 0\n')
    def test_tcn_c1_n0(self):
        """ Test tcn c=1 n=0 """
        argv = ['-tcn', '-c', '1', '-n', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '0 0\n')
    def test_tcn_c1_n1(self):
        """ Test tcn c=1 n=1 """
        argv = ['-tcn', '-c', '1', '-n', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_tcn_c1_n2(self):
        """ Test tcn c=1 n=2 """
        argv = ['-tcn', '-c', '1', '-n', '2']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n0 1\n')
    def test_tcn_c2_n0(self):
        """ Test tcn c=2 n=0 """
        argv = ['-tcn', '-c', '2', '-n', '0']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '0 0\n')
    def test_tcn_c2_n1(self):
        """ Test tcn c=2 n=1 """
        argv = ['-tcn', '-c', '2', '-n', '1']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '1 0\n')
    def test_tcn_c2_n2(self):
        """ Test tcn c=2 n=2 """
        argv = ['-tcn', '-c', '2', '-n', '2']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '2 1\n0 1\n')
    def test_tcn_c2_n5(self):
        """ Test tcn c=2 n=5 """
        argv = ['-tcn', '-c', '2', '-n', '5']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '5 4\n0 1\n0 2\n1 3\n1 4\n')
    def test_tcn_c2_n6(self):
        """ Test tcn c=2 n=6 """
        argv = ['-tcn', '-c', '2', '-n', '6']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '6 5\n0 1\n0 2\n1 3\n1 4\n2 5\n')
    def test_tcn_c2_n7(self):
        """ Test tcn c=2 n=7 """
        argv = ['-tcn', '-c', '2', '-n', '7']
        with patch('sys.stdout', new=StringIO()) as redirect:
            gen_graph.main(argv)
            self.assertEqual(redirect.getvalue(), '7 6\n0 1\n0 2\n1 3\n1 4\n2 5\n2 6\n')

if __name__ == '__main__':
    unittest.main()
