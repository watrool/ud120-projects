#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    ### your code goes here

    import numpy as np
    error = [0] * len(predictions)
    for idx, val in enumerate(ages):
        error[idx] = abs(predictions[idx] - net_worths[idx])[0]
    pointsToBeRemoved = sorted(error)
    pointsToBeRemoved.reverse()
    pointsToBeRemovedIndex = [0] * 9
    for idx, val in enumerate(pointsToBeRemoved):
        if (idx < 9):
            pointsToBeRemovedIndex[idx] = error.index(val)
    ages = np.array([s for idx, s in enumerate(ages) if idx not in pointsToBeRemovedIndex]).reshape(-1,1)
    net_worths = np.array([s for idx, s in enumerate(net_worths) if idx not in pointsToBeRemovedIndex]).reshape(-1,1)
    error = np.array([s for idx, s in enumerate(error) if idx not in pointsToBeRemovedIndex]).reshape(-1,1)
    cleaned_data = [ages, net_worths, error]
    return cleaned_data
