"""

Integrated example for nosql databases

"""

import learn_data
import simple_script
import mongodb_script
import redis_script
import neo4j_script
import persistence_serialization
import utilities
import pickle_temp_data


def showoff_databases():
    """
    Here we illustrate basic interaction with nosql databases
    """

    log = utilities.configure_logger('default', '../logs/nosql_dev.log')

    log.info("Mongodb example to use data from Furniture module, so get it")
    furniture = learn_data.get_furniture_data()

    mongodb_script.run_example(furniture)

    log.info("Other databases use data embedded in the modules")

    redis_script.run_example()
    neo4j_script.run_example()
    temperatures = pickle_temp_data.get_pickle_data()
    persistence_serialization.pickle_data(temperatures)
    simple_script.run_example(furniture)

if __name__ == '__main__':
    """
    orchestrate nosql examples
    """

    showoff_databases()
