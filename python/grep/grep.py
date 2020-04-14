import sys
import re

class Record:
    def __init__(self, is_match, line, line_number, file_index):
        self.is_match = is_match
        self.line = line
        self.line_number= line_number
        self.file_index = file_index

def grep(pattern, flags, files):
    records = []
    match_count = 0
    with open(files[0], "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            pat, txt = pattern, lines[i].strip()
            match = 0
            res = lines[i]
            if "i" in flags:
                pat, txt = pat.lower(), txt.lower()
            if "x" in flags:
                if pat == txt:
                    match = 1
            else:
                if pat in txt:
                    match = 1
            match_count += match
            records.append(Record(match, lines[i], i+1, 0))

    records = sorted(records, key=lambda record: record.is_match)
    target_range = [0, len(records)]
    if "v" in flags:
        target_range[1] = len(records)-match_count
    else:
        target_range[0] = len(records)-match_count

    if target_range[0] == target_range[1]:
        return ""

    if "l" in flags:
        return files[0] + "\n"
    else:
        target_lines = []
        target_lines_indexed = []
        for record in records[target_range[0]:target_range[1]]:
            if "n" in flags:
                target_lines_indexed.append(str(record.line_number) + ":" + record.line)
            else:
                target_lines.append(record.line)

        if "n" in flags:
            return "".join(target_lines_indexed)
        else:
            return "".join(target_lines)

    """
    # raise exception on illegal flags
    allowed_flags = "nlivx"
    flags = "".join(re.split("[^a-zA-Z]", flags)).lower()
    for flag in flags:
        if flag not in allowed_flags:
            raise Exception("grep.py: invalid option -- ", flag)

    # 'data' keeps all lines in a list of dictionary objects
    # each object represents a line as 'line', its match status as 'match'––1 for
    # a match and 0 for a mismatch, line number as a 1-based index in its parent file,
    # and a 0-based index reference to the parent file name in 'files'.

    data = []
    match_count = 0
    for i in range(len(files)):
        with open(files[i], "r") as stdin:
            lines = stdin.readlines()
            for j in range(len(lines)):
                pat, txt = pattern, lines[j].strip()
                if "i" in flags:
                    pat, txt = pat.lower(), txt.lower()
                match = 1 if pat in txt else 0
                if "x" in flags:
                    match = 1 if pat == txt else 0
                match_count += match
                data.append({"match": match, "line": lines[j], "line_index": j+1, "file_index": i})

    # sort lines by match status
    data = sorted(data, key=lambda item: (item["match"]))

    # find the target range/matching lines or mismatching lines
    target_range = [0, len(data)]
    if "v" in flags:
        target_range[1] = len(data)-match_count
    else:
        target_range[0] = len(data)-match_count

    # return empty string if target range is empty
    if target_range[0] == target_range[1]:
        return ""

    target_lines = []
    target_lines_indexed = []

    # we need a 'previous' filename to compare w/ so we keep each file name once.
    target_files = [files[data[target_range[0]]["file_index"]]]

    for item in data[target_range[0]:target_range[1]]:
        if "l" in flags:
            file = files[item["file_index"]]
            if file != target_files[-1]:
                target_files.append(file)
        else:
            file = "" if len(files) == 1 else files[item["file_index"]] + ":"
            if "n" in flags:
                target_lines_indexed.append(file + str(item["line_index"]) + ":" + item["line"])
            else:
                target_lines.append(file + item["line"])

    # return found targets
    if target_lines:
        return "".join(target_lines)
    elif target_files and "l" in flags:
        return "\n".join(target_files) + "\n"
    else:
        return "".join(target_lines_indexed)
    """
