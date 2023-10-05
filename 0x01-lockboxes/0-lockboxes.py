#!/usr/bin/python3
# 0-lockboxes.py
# You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

# Write a method that determines if all the boxes can be opened.

#     Prototype: def canUnlockAll(boxes)
#     boxes is a list of lists
#     A key with the same number as a box opens that box
#     You can assume all keys will be positive integers
#         There can be keys that do not have boxes
#     The first box boxes[0] is unlocked
#     Return True if all boxes can be opened, else return False

"""_summary_a function that determines if all the boxes can be opened
    """
def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    if not boxes:
        return False
    if type(boxes) is not list:
        return False
    if len(boxes) == 1:
        return True
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False