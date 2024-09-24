def merge_sort_toys(toys):
    # If the pile has more than 1 toy, we split and sort
    if len(toys) > 1:
        mid = len(toys) // 2  # Find the middle point
        
        # Split the pile into two halves
        left_half = toys[:mid]
        right_half = toys[mid:]

        # Sort the left and right halves
        merge_sort_toys(left_half)
        merge_sort_toys(right_half)

        i = j = k = 0  # i = left half index, j = right half index, k = toys list index

        # Compare and merge the toys
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                toys[k] = left_half[i]
                i += 1
            else:
                toys[k] = right_half[j]
                j += 1
            k += 1

        # If there are any toys left in the left half, add them to the list
        while i < len(left_half):
            toys[k] = left_half[i]
            i += 1
            k += 1

        # If there are any toys left in the right half, add them to the list
        while j < len(right_half):
            toys[k] = right_half[j]
            j += 1
            k += 1

# Example:
toys = [5, 2, 9, 1, 7, 3]  # The sizes of toys (from smallest to biggest)
merge_sort_toys(toys)
print("Sorted toy sizes:", toys)
