import re
def tally(rows):
    table = dict()
    for row in rows:
        elts = re.split(";", row)
        if elts[0] not in table:
            table[elts[0]] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
        if elts[1] not in table:
            table[elts[1]] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

        if elts[2] == "win":
            table[elts[0]]["W"] += 1
            table[elts[0]]["P"] += 3
            table[elts[1]]["L"] += 1
        elif elts[2] == "loss":
            table[elts[1]]["W"] += 1
            table[elts[1]]["P"] += 3
            table[elts[0]]["L"] += 1
        elif elts[2] == "draw":
            table[elts[0]]["D"] += 1
            table[elts[0]]["P"] += 1
            table[elts[1]]["D"] += 1
            table[elts[1]]["P"] += 1

        table[elts[0]]["MP"] += 1
        table[elts[1]]["MP"] += 1

    result = ["Team                           | MP |  W |  D |  L |  P"]
    for team in sorted(sorted(table), key=lambda name: table[name]["P"], reverse=True):
        row = "{:<30s} | {:>2d} | {:>2d} | {:>2d} | {:>2d} | {:>2d}".format(
                team, table[team]["MP"], table[team]["W"], table[team]["D"],
                table[team]["L"], table[team]["P"])
        result.append(row)
    return result
