import argparse
from gradebook.storage import load_data, save_data
from gradebook.service import (
    add_student, add_course, enroll,
    add_grade, list_students, list_courses,
    list_enrollments, compute_average, compute_gpa
)
def main():
    parser = argparse.ArgumentParser(description="Gradebook CLI")
    subparsers = parser.add_subparsers(dest="command")

    
    p1 = subparsers.add_parser("add-student")
    p1.add_argument("--name", required=True)

    
    p2 = subparsers.add_parser("add-course")
    p2.add_argument("--code", required=True)
    p2.add_argument("--title", required=True)

    
    p3 = subparsers.add_parser("enroll")
    p3.add_argument("--student-id", required=True, type=int)
    p3.add_argument("--course", required=True)

    
    p4 = subparsers.add_parser("add-grade")
    p4.add_argument("--student-id", required=True, type=int)
    p4.add_argument("--course", required=True)
    p4.add_argument("--grade", required=True, type=float)

    
    p5 = subparsers.add_parser("list")
    p5.add_argument("type", choices=["students", "courses", "enrollments"])

    
    p6 = subparsers.add_parser("avg")
    p6.add_argument("--student-id", required=True, type=int)
    p6.add_argument("--course", required=True)

    
    p7 = subparsers.add_parser("gpa")
    p7.add_argument("--student-id", required=True, type=int)

    args = parser.parse_args()
    data = load_data()

if __name__ == "__main__":
    main()