def min_time_to_visit_all_points(points):
    '''
    Logic : We can either move from both axis or only one axis. If we want to move from (1,1) to (2,4). 
    We go both axis (2,2), then after only one axis (2,3) then (2,4). Hence time = 3 = 4-1
    '''
    x_i, y_i = points.pop()
    time_taken = 0

    while points: 
        x_f, y_f = points.pop()
        time_taken += max(abs(x_f-x_i), abs(y_f-y_i))
        x_i, y_i = x_f, y_f
    return time_taken


if __name__ == "__main__":
    points = [[1,1],[-3, 5],[-5, 4]]
    print(min_time_to_visit_all_points(points))
