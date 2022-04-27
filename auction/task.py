class Task:
    """
    Abstraction of the Tasks that must be assigned
    """

    def __init__(self, name: str, cpu: int):
        """
        Create a new Task

        :param name: The task name.
        :param cpu: The required amount of *cpu* in the agent where the task will be executed.
        """
        self.name = name
        self.cpu = cpu

    @property
    def name(self):
        """
        The task name.
        """
        return self._name

    @name.setter
    def name(self, value: int):
        """
        Set the task name.
        """
        if not type(value) == str:
            raise TypeError("The name must be an str.")

        self._name = value

    @property
    def cpu(self):
        """
        The amount cpu required.
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

