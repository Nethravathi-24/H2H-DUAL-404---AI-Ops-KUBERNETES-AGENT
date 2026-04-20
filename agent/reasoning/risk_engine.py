def calculate_risk(summary):
    
    failing = summary["failing"]

    if failing == 0:
        return "LOW", "🟢"

    elif failing <= 2:
        return "MEDIUM", "🟡"

    else:
        return "HIGH", "🔴"