def convert_to_list(value):
    """Convert value to list if not"""
    if isinstance(value, list):
        return value
    else:
        return [value]
