''' Understand
    1) We have a list of tuples, each with a start and end time
    2) Find the smallest gap between the consecutive work sessions
    Plan
    1) Subtract next tuples' start time with previous session's end time
'''
def find_smallest_gap(work_sessions):
    gap = 0
    end_time = 0
    for i in range(0, len(work_sessions)):
        if i == 0:
            end_time = (work_sessions[i][1]) - 40
            continue
        if i == 1:
            gap = (work_sessions[i][0]) - 40
            end_time = (work_sessions[i][1]) - 40
            continue
        if (work_sessions[i][0] - 40) - end_time < gap:
            gap = (work_sessions[i][0] - 40) - end_time
            end_time = (work_sessions[i][1] - 40)
    return gap
# Test Cases
work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))
