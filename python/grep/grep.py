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

    def process_line(line, line_number, file_index):
        pat, txt = pattern, line.strip()
        match = 0
        res = lines[i]
        if "i" in flags:
            pat, txt = pat.lower(), txt.lower()
        if "x" in flags and pat == txt:
            match = 1
        if "x" not in flags and pat in txt:
            match = 1
        records.append(Record(match, line, line_number, file_index))
        return match

    for j in range(len(files)):
        file = open(files[j], "r")
        lines = file.readlines()
        for i in range(len(lines)):
            match_count += process_line(lines[i], i+1, j)
        file.close()

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
        curr_file = files[record.file_index]
        if "l" in flags and curr_file != target_files[-1]:
            target_files.append(curr_file)
            continue

        curr_file = "" if len(files) == 1 else curr_file+":"
        if "n" in flags:
            target_lines_indexed.append(curr_file+str(record.line_number) + ":" + record.line)
        else:
            target_lines.append(curr_file+record.line)

    if "l" in flags:
        return "\n".join(target_files) + "\n"
    elif "n" in flags:
        return "".join(target_lines_indexed)
    else:
        return "".join(target_lines)
