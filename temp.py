def mean_temperature(data):
    """
    Get the mean temperature

    Args:
        data (pandas.DataFrame): A pandas dataframe with air temperature measurements.

    Returns:
        The mean air temperature (float)
    """
    temperatures = data['Air temperature (degC)']
    return float(sum(temperatures)/len(temperatures))