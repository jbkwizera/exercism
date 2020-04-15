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
    for j in range(len(files)):
        with open(files[j], "r") as file:
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
                records.append(Record(match, lines[i], i+1, j))

    records = sorted(records, key=lambda record: record.is_match)

    target_range = [0, len(records)]
    if "v" in flags:
        target_range[1] = len(records)-match_count
    else:
        target_range[0] = len(records)-match_count

    if target_range[0] == target_range[1]:
        return ""

    target_lines = []
    target_lines_indexed = []
    target_files = [files[records[target_range[0]].file_index]]
    for record in records[target_range[0]:target_range[1]]:
        if "l" in flags:
            file = files[record.file_index]
            if file != target_files[-1]:
                target_files.append(file)
        else:
            parent_file = "" if len(files) == 1 else files[record.file_index]+":"
            if "n" in flags:
                target_lines_indexed.append(parent_file+str(record.line_number) + ":" + record.line)
            else:
                target_lines.append(parent_file+record.line)

    if "l" in flags:
        return "\n".join(target_files) + "\n"
    elif "n" in flags:
        return "".join(target_lines_indexed)
    else:
        return "".join(target_lines)
