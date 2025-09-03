def get_input():
    n, m = map(int, input().split())

    preferences = {}
    # Example of how preferences dict will look like
    # {'A': ['B'], 'B': ['A']}

    for _ in range(n):
        tokens = input().split()
        vertex = tokens[0]
        prefs = tokens[1:]
        preferences[vertex] = prefs 
    return n, m, preferences

def spm():
    n, m, preferences = get_input()
    items = list(preferences.items())
    # Create two separate dictionaries
    rejectors_preferences = dict(items[:len(items)//2]) # Split the list of tuples in half
    proposers_preferences = dict(items[len(items)//2:]) # Split the list of tuples in half
    free_proposers = list(proposers_preferences.keys())
    next_proposal_index = {p: 0 for p in proposers_preferences}
    # next_proposal_index[proposer] gives the index of the next rejector to propose t

    matches = {}

    inverse_matches = {}

    while free_proposers:
        proposer = free_proposers.pop(0)

        if next_proposal_index[proposer] >= len(proposers_preferences[proposer]):
            continue
        r = proposers_preferences[proposer][next_proposal_index[proposer]]
        next_proposal_index[proposer] += 1

        if r not in matches:
            matches[r] = proposer
            inverse_matches[proposer] = r

        else:
            current_partner = matches[r]
            if rejectors_preferences[r].index(proposer) < rejectors_preferences[r].index(current_partner):
                # r prefers p over current partner
                matches[r] = proposer
                inverse_matches[proposer] = r

                # the old partner becomes free again
                del inverse_matches[current_partner]
                free_proposers.append(current_partner)
            else:
                free_proposers.append(proposer)  # rejected, stays unmatched
    
    # Check if we have a perfect matching
    if len(matches) != len(rejectors_preferences) or len(inverse_matches) != len(proposers_preferences):
        print("-")
    else:
        # Print the matching, one edge per line
        for rejector, proposer in matches.items():
            print(f"{rejector} {proposer}")

spm()