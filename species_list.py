def filter_species(df, species_name):
    """
    Filter a DataFrame to only include rows with a specific species name.

    Args:
        df (pandas.DataFrame): The DataFrame to filter.
        species_name (str): The name of the species to filter for.

    Returns:
        pandas.DataFrame: A new DataFrame containing only the rows with the specified species name.
    
    EXCEPTIONS:
        ValueError: If the species name is not found in the DataFrame.


    Examples:
        >>> filter_species(df, 'CERISAFERA')
        
        
    """
    return df[df['species_name'] == species_name] & (df['street_side_name'] != 'MED')]