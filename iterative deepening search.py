def iterative_deepening_dfs(start, target):
    depth = 1
    bottom_reached = False
    while not bottom_reached:
        result, bottom_reached = iterative_deepening_dfs_rec(start, target, 0, depth)
        if result is not None:
            return result

        depth *= 2
        print("Increasing depth to " + str(depth))

    return None


def iterative_deepening_dfs_rec(node, target, current_depth, max_depth):
    print("Visiting Node " + str(node["value"]))

    if node["value"] == target:
        # We have found the goal node we we're searching for
        print("Found the node we're looking for!")
        return node, True

    if current_depth == max_depth:
        print("Current maximum depth reached, returning...")
        # We have reached the end for this depth...
        if len(node["children"]) > 0:
            # ...but we have not yet reached the bottom of the tree
            return None, False
        else:
        else:
            return None, True

    # Recurse with all children
    bottom_reached = True
    for i in range(len(node["children"])):
        result, bottom_reached_rec = iterative_deepening_dfs_rec(node["children"][i], target, current_depth + 1,
                                                                 max_depth)
        if result is not None:
            # We've found the goal node while going down that child
            return result, True
        bottom_reached = bottom_reached and bottom_reached_rec

    # We've gone through all children and not found the goal node
    return None, bottom_reached