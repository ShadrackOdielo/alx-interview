#!/usr/bin/python3
# 0-lockboxes.py

"""a function that determines if all the boxes can be opened.
boxes is a list of lists"""

def canUnlockAll(boxes):
    """Determines if all the boxes can be opene"""
    if not boxes:
        return False
    if len(boxes) == 1:
        return True
    keys = boxes[0]
    for i in range(1, len(boxes)):
        for j in range(len(boxes[i])):
            if boxes[i][j] not in keys and boxes[i][j] < len(boxes):
                keys.append(boxes[i][j])
    for i in range(1, len(boxes)):
        if i not in keys:
            return False
    return True
