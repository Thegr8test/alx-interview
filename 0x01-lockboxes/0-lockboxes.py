#!/usr/bin/python3

def canUnlockAll(boxes):
    '''
    Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.

    :param boxes: A list of lists, where each inner list represents a box,
                  and the indices in the inner list are the keys to other boxes.
    :type boxes: list of lists

    :return: True if all boxes can be unlocked, False otherwise.
    :rtype: bool
    '''
    # Get the total number of boxes
    n = len(boxes)

    # Initialize a set to keep track of seen boxes, starting with box 0 as seen
    seen_boxes = set([0])

    # Initialize a set to keep track of unseen boxes, starting with the keys in box 0
    unseen_boxes = set(boxes[0]).difference(set([0]))

    # Continue until there are no more unseen boxes
    while len(unseen_boxes) > 0:
        # Get the index of an unseen box
        boxIdx = unseen_boxes.pop()

        # Check if the box index is out of bounds or already seen, and skip it if so
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue

        # Add the current box index to the seen set
        if boxIdx not in seen_boxes:
            seen_boxes.add(boxIdx)

        # Add the keys in the current box to the unseen set
        unseen_boxes = unseen_boxes.union(boxes[boxIdx])

    # If the number of seen boxes equals the total number of boxes, return True (all boxes can be unlocked)
    return n == len(seen_boxes)
