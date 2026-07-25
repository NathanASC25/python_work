def lineup(artists, set_times):
    lineup = dict()
    i = 0
    while i < len(artists):
        lineup[artists[i]] = set_times[i]
        i += 1
    return lineup
# Test Cases
artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))
