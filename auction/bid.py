class Bid:
    """
    Abstraction of the Bid
    """

    def __init__(self, agent_name: str, task_name: str, price: float, time: int):
        """
        Create a new Task

        :param agent_name: The name of the agent.
        :param task_name: The name of the task.
        :param price: The price that the agent will pay.
        :param time: The time when the agent make the bid.
        """
        self.agent_name = agent_name
        self.task_name = task_name
        self.price = price
        self.time = time

    @property
    def agent_name(self):
        """
        The agent.
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value: str):
        """
        Set the task.
        """
        if not type(value) == str:
            raise TypeError("The agent must be a str.")

        self._agent_name = value

    @property
    def task_name(self):
        """
        The task.
        """
        return self._task_name

    @task_name.setter
    def task_name(self, value: str):
        """
        Set the task.
        """
        if not type(value) == str:
            raise TypeError("The task must be a str.")

        self._task_name = value

    @property
    def price(self):
        """
        The offered price.
        """
        return self._price

    @price.setter
    def price(self, value: float):
        """
        Set the value.
        """
        if not type(value) == float:
            raise TypeError("The price must be a float.")

        self._price = value

    @property
    def time(self):
        """
        The bid time.
        """
        return self._time

    @time.setter
    def time(self, value: float):
        """
        Set the time.
        """
        if not type(value) == int:
            raise TypeError("The time must be an int.")

        self._time = value

