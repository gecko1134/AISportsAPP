import pulp

def optimize_schedule(requests, resources, time_slots):
    prob = pulp.LpProblem("ScheduleOptimizer", pulp.LpMaximize)
    x = pulp.LpVariable.dicts("x", (requests.index, time_slots), cat="Binary")
    prob += pulp.lpSum(requests.loc[r, 'value'] * x[r][t] for r in requests.index for t in time_slots)
    for r in requests.index:
        prob += pulp.lpSum(x[r][t] for t in time_slots) <= 1
    for t in time_slots:
        prob += pulp.lpSum(requests.loc[r,'resources_needed'] * x[r][t] for r in requests.index) <= resources[t]
    prob.solve()
    schedule = [(r, t) for r in requests.index for t in time_slots if x[r][t].value() == 1]
    return schedule
