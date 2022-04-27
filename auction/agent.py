import random
from beautifultable import BeautifulTable

from auction.task import Task
from auction.bid import Bid


class Agent:
    """
    Abstraction of the Agent that will execute the tasks.
    """

    def __init__(self, name: str, cpu: int, cost: float):
        """
        Create a new Agent

        :param name: The agent name.
        :param cpu: The available *cpu* in the agent.
        :param cost: The cost of cpu unit.
        """
        self.name = name
        self.cpu = cpu
        self.cost = cost
        self._neighbours = {}

        # all the task in the environment
        self._tasks = {}

        # all the bided tasks by the agent
        self._bidding_tasks = {}

        # the local winning list
        self._winning_list = {}

    @property
    def winning_list(self):
        """
        The winning list.
        """
        return self._winning_list

    @property
    def name(self):
        """
        The task name.
        """
        return self._name

    @name.setter
    def name(self, value: str):
        """
        Set the agent name.
        """
        if not type(value) == str:
            raise TypeError("The name must be an str.")

        self._name = value

    @property
    def cpu(self):
        """
        The agent total cpu.
        """
        return self._cpu

    @cpu.setter
    def cpu(self, value: int):
        """
        Set the amount of cpu.
        """
        if not type(value) == int:
            raise TypeError("The cpu must be an int.")

        self._cpu = value

    @property
    def cost(self):
        """
        The cost of cpu unit.
        """
        return self._cost

    @cost.setter
    def cost(self, value: int):
        """
        Set the cost of cpu unit.
        """
        if not type(value) == float:
            raise TypeError("The cost must be a float.")

        self._cost = value

    def receive_tasks(self, tasks: [Task]):
        """
        Receive a list of tasks

        :param tasks: List with all tasks that the agent can bid.
        """
        self._tasks = tasks

    def add_neighbour(self, agent):
        """
        Add a neighbour agent
        """
        self._neighbours[agent.name] = agent

    def count_neighbour(self):
        """
        Count the neighbour agent
        """
        return len(self._neighbours)

    def available_cpu(self):
        """
        Compute the amount of cpu available by the agent

        :return int
        """
        cpu = self.cpu
        for task_name, bid in self._bidding_tasks.items():
            # only for bids above 0
            if bid.price > 0:
                cpu -= self._tasks[task_name].cpu

        return cpu

    def send_bids(self, time: int):
        """
        Send the winning list to the agent neighbours

        :param time: The bid creation time.
        """
        for neighbour_name, neighbour in self._neighbours.items():
            neighbour.receive_bids(neighbour, self._winning_list, time)

    def receive_bids(self, agent, winning_bids: {}, time: int):
        """
        Receive the bids from a neighbour agent and update the local winning list.

        :param agent: The agent object that send the winning list.
        :param winning_bids: The list of the winning bids for the agent.
        :param time: The bid creation time.
        """

        for task_name, bid in winning_bids.items():
            if task_name in self._winning_list:
                # only update the winner when higher bids arrives
                if bid.price > self._winning_list[task_name].price:
                    if self._winning_list[task_name].agent_name == self.name:
                        # Create a new bid
                        new_bid = self.create_bid(
                            task=self._tasks[task_name],
                            time=time,
                            actual_price=bid.price
                        )

                        if new_bid:
                            # Update a local winner
                            self.set_local_winner(new_bid)
                            continue
                    else:
                        self.set_local_winner(bid)

    def add_tasks(self, tasks: [Task]):
        """
        Add multiples tasks to the agent
        """
        for task in tasks:
            self.add_task(task)

    def add_task(self, task: Task):
        """
        Add a task to agent bid

        :param task: The task object
        :return None
        """
        duplicated = False
        for task_name, aux_task in self._tasks.items():
            if task_name == task.name:
                duplicated = True

        if duplicated:
            raise TypeError("The task {} already add in the agent.".format(task.name))

        self._tasks[task.name] = task

    def set_local_winner(self, bid: Bid):
        """
        Set an agent as local winner for a task

        :param bid: The bid object
        :return None
        """
        self._winning_list[bid.task_name] = bid

    def create_bids(self, time: int):
        """
        Create a bid for all the tasks

        :param time: The bid creation time.
        """
        for task_name, task in self._tasks.items():
            bid = self.create_bid(
                task=task,
                time=time
            )

            if bid:
                self._bidding_tasks[task.name] = bid

                if task_name not in self.winning_list:
                    self.set_local_winner(bid)

        return self._bidding_tasks

    def create_bid(self, task: Task, time: int, actual_price=0):
        """
        Create a bid for a task with the max willing price that the agent will pay.

        For an agent bid a task the cpu available in the agent should be greater than the cpu required by the task.

        The agent bid value will be inversely proportional to with the CPU resource available. Agent with higher
        resources will pay more for the task. (load balance strategy)

        :param task: The task object.
        :param time: The bid creation time.
        :param actual_price: The actual bid price.

        :return None or bid
        """
        bid = None

        available_cpu = self.available_cpu()

        print(task.name, self.name)

        if available_cpu >= task.cpu:

            price = ((self.cpu - task.cpu) / self.cpu) * self.cost * task.cpu

            if price < actual_price:
                if random.choice([True, False]):
                    # increase the price in one
                    price = actual_price + 1.0
                else:
                    # remove the task from the bidding list
                    if task.name in self._bidding_tasks:
                        print("sssssssssssssss")
                        del self._bidding_tasks[task.name]
                    return None

            bid = Bid(
                agent_name=self.name,
                task_name=task.name,
                price=price,
                time=time
            )
        else:
            bid = Bid(
                agent_name=self.name,
                task_name=task.name,
                price=0.0,
                time=time
            )

        return bid

    def print_winning_list(self):

        table = BeautifulTable()

        table.columns.header = [
            "Agent",
            "Task",
            "Price",
            "Time"
        ]

        for task_name, bid in self._winning_list.items():
            table.rows.append([
                bid.agent_name,
                task_name,
                bid.price,
                bid.time
            ])


        print("Winning List in Agent {}".format(self.name))
        print(table)