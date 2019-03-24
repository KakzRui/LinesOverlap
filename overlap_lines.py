def overlap(l1, l2):
    try:
        l1 = tuple([int(float(i)) for i in l1])
        l2 = tuple([int(float(i)) for i in l2])
        for i in range(2):
            if l1[0] >= 0 and l2[0] >= 0 or l2[0] >= 0 and l2[1] >= 0:
                if l2[i] <= l1[0] or l2[i] <= l1[1]:
                    return '{} and {} overlaps on x-axis'.format(l1, l2)
            else:
                if l2[i] >= l1[0] or l2[i] >= l1[1]:
                    return '{} and {} overlaps on x-axis'.format(l1, l2)
        return '{} and {} not overlaps on x-axis'.format(l1, l2)
    except ValueError:
        return 'Please give valid co-ordinates'
