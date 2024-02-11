import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    """
    Most start ups fail. 
    But some markets, ideas, and teams are better than others.
    After Learning about start ups in class, I want to figure
    out some associated probabilities
    
    Prior: 9/10 start ups fail, 1/10 start ups are successful

    From a naive perspective, in order to have a successful company,
    3 things need to align. The right market, idea, and team.
    
    likelihood: given a good start up, whats the probability they have...
    a good market? : 9.5/10
        - There are always avenues to create more value. However,
        to find a good market for a start-up specifically requires
        a niche, and small but rapidly growing market. Any larger and
        a larger company will already have its eye on it.
        - Successful companies need good markets
    a good idea/product? : 5/10
        - Given enough money and time, most will be able to produce
        a good product either through hiring others or engineering
        - however, good ideas need to look bad to others or there will
        be too much competition.
        - So having a good idea right away is not super important
    a good team? : 7.5/10
        - Finding the right team is hard...
        - Having a good team is super important
    
    """

    prior = 0.1
