def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    if not values:
        return []

    if len(values) == 1:
        return [0.0]
    
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    
    def get_median(lst):
        length = len(lst)
        if length % 2 != 0:
            return lst[length // 2]
        else:
            return (lst[length // 2 - 1] + lst[length // 2]) / 2.0

    overall_median = get_median(sorted_vals)
    
    mid = n // 2
    if n % 2 != 0:
        lower_half = sorted_vals[:mid]
        upper_half = sorted_vals[mid + 1:]
    else:
        lower_half = sorted_vals[:mid]
        upper_half = sorted_vals[mid:]
        
    q1 = get_median(lower_half)
    q3 = get_median(upper_half)
    
    iqr = q3 - q1
    
    if iqr == 0:
        return [float(x - overall_median) for x in values]
    else:
        return [float(x - overall_median) / iqr for x in values]