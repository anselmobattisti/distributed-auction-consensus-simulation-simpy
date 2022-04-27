import unittest
from auction.agent import Agent
from auction.task import Task
import random


class AgentTest(unittest.TestCase):

    name = None
    cpu = None
    cost = None
    agent = None

    @classmethod
    def setUpClass(cls):
        cls.name = "ag_1"
        cls.cpu = 1000
        cls.cost = 2.0

        cls.agent = Agent(
            name=cls.name,
            cpu=cls.cpu,
            cost=cls.cost
        )

    def test_creation(self):
        self.assertEqual(self.agent.name, self.name)
        self.assertEqual(self.agent.cpu, 1000)
        self.assertEqual(self.agent.cost, 2)

    def test_create_bid(self):
        """
        Verify if the cpu available in the agent.
        """
        t_1 = Task(
            name="t_1",
            cpu=10
        )

        ag_1 = Agent(
            name="ag_1",
            cpu=100,
            cost=1.0
        )

        bid = ag_1.create_bid(
            task=t_1,
            time=1
        )

        self.assertEqual(bid.price, 9.0)

    def test_create_bids(self):
        """
        Verify if the cpu available in the agent.
        """
        t_1 = Task(
            name="t_1",
            cpu=10
        )

        t_2 = Task(
            name="t_2",
            cpu=20
        )

        ag_1 = Agent(
            name="ag_1",
            cpu=100,
            cost=1.0
        )

        ag_1.add_task(task=t_1)
        ag_1.add_task(task=t_2)

        bids = ag_1.create_bids(time=1)

        self.assertEqual(bids['t_1'].price, 9.0)
        self.assertEqual(bids['t_2'].price, 16.0)

    def test_add_neighbour(self):
        """
        Test the add of neighbours to agent
        """
        ag_1 = Agent(
            name="ag_1",
            cpu=100,
            cost=1.0
        )

        ag_2 = Agent(
            name="ag_2",
            cpu=100,
            cost=1.0
        )

        ag_3 = Agent(
            name="ag_3",
            cpu=100,
            cost=1.0
        )

        ag_1.add_neighbour(ag_2)
        ag_1.add_neighbour(ag_3)
        ag_2.add_neighbour(ag_1)
        ag_3.add_neighbour(ag_1)

        self.assertEqual(ag_1.count_neighbour(), 2)
        self.assertEqual(ag_2.count_neighbour(), 1)
        self.assertEqual(ag_3.count_neighbour(), 1)

    def test_auction(self):
        """
        Verify if agents find a consensus
        """

        ag_1 = Agent(
            name="ag_1",
            cpu=100,
            cost=1.0
        )

        ag_2 = Agent(
            name="ag_2",
            cpu=100,
            cost=2.0
        )

        t_1 = Task(
            name="t_1",
            cpu=10
        )

        ag_1.add_task(t_1)
        ag_2.add_task(t_1)

        ag_1.add_neighbour(ag_2)
        ag_2.add_neighbour(ag_1)

        now = 1
        ag_1.create_bids(time=now)
        # ag_1.print_winning_list()

        ag_2.create_bids(time=now)
        # ag_2.print_winning_list()

        ag_1.send_bids(time=now)
        ag_2.send_bids(time=now)

        # final winning
        print("Final Winning")
        ag_1.print_winning_list()
        ag_2.print_winning_list()

        self.assertEqual(ag_1.winning_list['t_1'].agent_name, 'ag_2')

    def test_auction_2(self):
        """
        Verify if agents find a consensus
        """

        random.seed(10)

        ag_1 = Agent(name="ag_1", cpu=100, cost=1.0)
        ag_2 = Agent(name="ag_2", cpu=100, cost=2.0)
        ag_3 = Agent(name="ag_3", cpu=100, cost=1.0)

        t_1 = Task(name="t_1", cpu=10)

        ag_1.add_task(t_1)
        ag_2.add_task(t_1)
        ag_3.add_task(t_1)

        ag_1.add_neighbour(ag_2)
        ag_2.add_neighbour(ag_1)

        ag_2.add_neighbour(ag_3)
        ag_3.add_neighbour(ag_2)

        now = 1
        ag_1.create_bids(time=now)
        # ag_1.print_winning_list()

        ag_2.create_bids(time=now)
        # ag_2.print_winning_list()

        ag_3.create_bids(time=now)
        # ag_2.print_winning_list()

        print("\n\n\nStep  1")
        ag_1.send_bids(time=now)
        ag_2.send_bids(time=now)
        ag_3.send_bids(time=now)
        ag_1.print_winning_list()
        ag_2.print_winning_list()
        ag_3.print_winning_list()

        print("\n\n\nStep  2")
        now = 2
        ag_1.send_bids(time=now)
        ag_2.send_bids(time=now)
        ag_3.send_bids(time=now)
        ag_1.print_winning_list()
        ag_2.print_winning_list()
        ag_3.print_winning_list()

        print("\n\n\nStep  3")
        now = 3
        ag_1.send_bids(time=now)
        ag_2.send_bids(time=now)
        ag_3.send_bids(time=now)
        ag_1.print_winning_list()
        ag_2.print_winning_list()
        ag_3.print_winning_list()

        self.assertEqual(ag_1.winning_list['t_1'].agent_name, 'ag_2')

    def test_auction_3(self):
        """
        Verify if agents find a consensus
        """

        random.seed(10)

        ag_1 = Agent(name="ag_1", cpu=100, cost=1.0)
        ag_2 = Agent(name="ag_2", cpu=100, cost=2.0)

        t_1 = Task(name="t_1", cpu=60)
        t_2 = Task(name="t_2", cpu=50)

        ag_1.add_tasks([t_1, t_2])
        ag_2.add_tasks([t_1, t_2])

        ag_1.add_neighbour(ag_2)
        ag_2.add_neighbour(ag_1)

        now = 1
        ag_1.create_bids(time=now)
        ag_2.create_bids(time=now)

        print("\n\nStep  1")
        ag_1.send_bids(time=now)
        ag_2.send_bids(time=now)
        ag_1.print_winning_list()
        ag_2.print_winning_list()

        print("\n\nStep  2")
        now = 2
        ag_1.send_bids(time=now)
        ag_2.send_bids(time=now)
        ag_1.print_winning_list()
        ag_2.print_winning_list()

        print("\n\nStep  3")
        now = 3
        ag_1.send_bids(time=now)
        ag_2.send_bids(time=now)
        ag_1.print_winning_list()
        ag_2.print_winning_list()

        self.assertEqual(ag_1.winning_list['t_1'].agent_name, 'ag_2')

