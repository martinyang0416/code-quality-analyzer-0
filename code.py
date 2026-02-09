def unhappyFriends(n, preferences, pairs):
    # Create a dictionary to map each person to their partner
    partner = {}
    for a, b in pairs:
        partner[a] = b
        partner[b] = a
    
    # Precompute the index of each friend in the preferences list for quick lookup
    prefs_index = [{} for _ in range(n)]
    for i in range(n):
        for idx, friend in enumerate(preferences[i]):
            prefs_index[i][friend] = idx
    
    count = 0
    # Check each person to see if they are 