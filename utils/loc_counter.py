def count_loc_comments(code_str):
    lines = code_str.splitlines()
    loc = sum(1 for line in lines if line.strip())
    comments = sum(1 for line in lines if line.strip().startswith("#"))
    return loc, comments
