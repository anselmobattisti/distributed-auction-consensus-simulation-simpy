import argparse
import simpy
from auction.auction_simulation import AuctionSimulation
from auction.helper import Helper


def main():

    parser = argparse.ArgumentParser(prog='SimPlacement')
    parser.add_argument('--config', default="./config.yml", help='Simulation config file')

    args = parser.parse_args()

    config = Helper.load_yml_file(args.config)

    # environment = Setup.load_entities(args.entities)

    env = simpy.Environment()

    se = AuctionSimulation(
        env=env,
        environment=environment
    )

    se.run()


if __name__ == "__main__":
    main()