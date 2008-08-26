__author__ = 'Tom Schaul, tom@idsia.ch and Daan Wierstra'

from datasets import AnBnCnDataSet
from pybrain.supervised import BackpropTrainer
from pybrain import FullConnection, Network, TanhLayer, LinearLayer


def testTraining():
    d = AnBnCnDataSet()
    hsize = 5
    n = Network()
    n.addModule(TanhLayer(hsize, name = 'h'))
    n.addOutputModule(LinearLayer(1, name = 'out'))
    n.addConnection(FullConnection(n['h'], n['out']))
    n.addRecurrentConnection(FullConnection(n['h'], n['h']))
    n.sortModules()
    assert n.indim == 0
    assert n.outdim == 1
    assert n.paramdim == hsize*(hsize+1)
    print n.params
    t = BackpropTrainer(n, learningrate = 0.1, momentum = 0.0, verbose = True)
    t.trainOnDataset(d, 20)
    print n.params

if __name__ == '__main__':
    testTraining()