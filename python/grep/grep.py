import sys
import re
def grep(pattern, flags, files):
    allowed_flags = "nlivx"
    flags = "".join(re.split("[^a-z]", flags))

    for flag in flags:
        if flag not in allowed_flags:
            raise Exception("grep.py: invalid option -- ", flag)

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
    data = sorted(data, key=lambda item: (item["match"], item["file_index"], item["line_index"]))
    target_range = [0, len(data)]
    if "v" in flags:
        target_range[1] = len(data)-match_count
    else:
        target_range[0] = len(data)-match_count
    if target_range[0] == target_range[1]:
        return ""

    target_lines = []
    target_lines_indexed = []
    target_files = [files[data[target_range[0]]["file_index"]]]

    for item in data[target_range[0]:target_range[1]]:
        if "l" in flags:
            file = files[item["file_index"]]
            if file != target_files[-1]:
                target_files.append(file)
        else:
            file = "" if len(files) == 1 else files[item["file_index"]]+":"
            if "n" in flags:
                target_lines_indexed.append(file + str(item["line_index"]) + ":" + item["line"])
            else:
                target_lines.append(file + item["line"])

    if target_lines:
        return "".join(target_lines)
    elif target_files and "l" in flags:
        return "\n".join(target_files) + "\n"
    else:
        return "".join(target_lines_indexed)

if __name__ == "__main__":
    pattern = sys.argv[1]
    flags   = sys.argv[2]
    files   = sys.argv[3:]

    print(grep(pattern, flags, files))
