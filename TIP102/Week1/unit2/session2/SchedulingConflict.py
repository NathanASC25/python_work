def identify_conflicts(venue1_schedule, venue2_schedule):
    conflicts = dict()
    for artist, time in venue2_schedule.items():
        if time == venue1_schedule.get(artist):
            conflicts[artist] = time
    return conflicts
# Test Cases
venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
