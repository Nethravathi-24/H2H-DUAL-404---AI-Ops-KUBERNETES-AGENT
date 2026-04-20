def generate_explanations(issues):
    
    explanations = []

    for issue in issues:

        if "crashing" in issue.lower():

            explanations.append(
                "🧠 Root Cause: Pod is crashing because the container "
                "is exiting immediately. Possible reasons include "
                "invalid startup command, missing dependencies, "
                "or application failure."
            )

        elif "memory" in issue.lower():

            explanations.append(
                "🧠 Root Cause: Pod is consuming high memory. "
                "Possible reasons include memory leak, "
                "large workload processing, or insufficient "
                "memory limits configured."
            )

        else:

            explanations.append(
                "🧠 Root Cause: Unknown issue detected. "
                "Further investigation required."
            )

    return explanations