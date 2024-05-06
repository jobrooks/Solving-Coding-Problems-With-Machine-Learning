import math

def connect_prob(N: int) -> float:
    """
    Calculates the probability that a randomly generated road network with N cities and N roads is connected.

    Args:
        N (int): The number of cities in the network.

    Returns:
        float: The probability that the network is connected.
    """

    # The probability that a single city is not connected to the rest of the network is (N-1)/N.
    single_city_not_connected_prob = (N - 1) / N

    # The probability that all N cities are not connected to the rest of the network is the product of the probabilities for each city.
    all_cities_not_connected_prob = single_city_not_connected_prob ** N

    # The probability that the network is connected is 1 minus the probability that it is not connected.
    connected_prob = 1 - all_cities_not_connected_prob

    return connected_prob