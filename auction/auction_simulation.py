import yaml
import simpy


class AuctionSimulation:
    """
    The simulation engine will execute the simulation based on the environment and configured parameters
    """

    def __init__(self, env: simpy.Environment, config, environment):
        """
        The auction simulation engine component.
        :param env: Simpy environment
        :param config: The total simulation configuration.
        :param environment: Object with all the configured simulation entities.
        """
        self.env = env
        self.config = config
        self.environment = environment
        self.duration = config['duration']
        self.seed = config['seed']

    def run(self):
        """
        Execute the simulation process
        :return: None
        """

        # Start the simulation
        self.env.process(self.simulate())

        # Run the simulation until the duration time limit
        self.env.run(until=self.duration)

    def simulate(self):
        """
        Execute the simulation main process
        :return: None
        """
        while True:
            # Execute the simulation tick of 1ms
            yield self.env.timeout(1)

            # Process the SFC Requests that arrived in the simulation time
            if self.env.now in self.environment['sfc_requests_arrival']:
                sfc_requests = self.environment['sfc_requests_arrival'][self.env.now]

                # Add all the SFC Requests to its domains
                for sfc_request in sfc_requests:
                    node_domain = self.environment['nodes_domain'][sfc_request.src.name]
                    node_domain.placement_cmp.add_sfc_request(sfc_request)

                for i, domain in self.environment['domains'].items():
                    ret = domain.placement_cmp.run()
                    print(ret)


