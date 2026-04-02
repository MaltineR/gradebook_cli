from gradebook.storage import load_data, save_data


def add_student(data, name):
    """Add a new student and return new id"""
    new_id = len(data["students"]) + 1
    data["students"][str(new_id)] = {"name": name}
    return data,new_id


def add_course(data, code, title):
    """Add a new course"""
    data["courses"][code] = {"title": title}
    return data


def enroll(data, student_id, course_code):
    """ Enroll a student in a course """
    data["enrollments"].append({
        "student_id": student_id,
        "course_code": course_code,
        "grades": []
    })
    return data


def add_grade(data, student_id, course_code, grade):
    """Add a grade to a student's course"""
    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_code"] == course_code:
            e["grades"].append(grade)


def list_students(data):
    """Return students sorted by name"""
    return sorted(data["students"].items(), key=lambda x: x[1]["name"])


def list_courses(data):
    """Return courses sorted by title"""
    return sorted(data["courses"].items(), key=lambda x: x[1]["title"])


def list_enrollments(data):
    """Return enrollments sorted by course code."""
    return sorted(data["enrollments"], key=lambda x: x["course_code"])


def compute_average(data, student_id, course_code):
    """Calculate average grade for a student in a course"""
    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_code"] == course_code:
            grades = e["grades"]
            return sum(grades) / len(grades) if grades else 0
    return 0


def compute_gpa(data, student_id):
    """Calculate GPA across all courses"""
    averages = [
        compute_average(data, student_id, e["course_code"])
        for e in data["enrollments"]
        if e["student_id"] == student_id
    ]
    return sum(averages) / len(averages) if averages else 0