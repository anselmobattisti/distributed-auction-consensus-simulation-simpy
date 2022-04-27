import os
import unittest
from auction.task import Task


class TaskTest(unittest.TestCase):

    name = None
    cpu = None
    mem = None
    task = None

    @classmethod
    def setUpClass(cls):
        cls.name = "t_1"
        cls.cpu = 100

        cls.task = Task(
            name=cls.name,
            cpu=cls.cpu,
        )

    def test_creation(self):
        self.assertEqual(self.task.name, self.name)
        self.assertEqual(self.task.cpu, 100)

    # def test_show(self):
    #     VNFHelper.show(self.vnf)
    #
    # def test_creation_from_conf(self):
    #     vnfs = VNFHelper.load(self.entities_file)
    #     for i, vnf in vnfs.items():
    #         VNFHelper.show(vnf)