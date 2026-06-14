def longest_common_prefix(strs):
    """Find the longest common prefix among strings."""
    if not strs:
        return ""
    prefix = strs[0]
    for i in strs[1:]:
        while not i.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


print(longest_common_prefix(["flower", "flow", "flight"]))