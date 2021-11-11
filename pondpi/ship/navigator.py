

class Course:
    course = None
    course_over_ground = None
    bearing = None
    heading = None
    crosstrack_distance = None
    turn = None
    track_error_angle = None
    drift_angle = None
    speed_over_ground = None


class Navigator:
    course = Course()

    def __init__(self):
        pass
