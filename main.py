import argparse
from gradebook.storage import load_data, save_data
from gradebook.service import (
    add_student, add_course, enroll,
    add_grade, list_students, list_courses,
    list_enrollments, compute_average, compute_gpa
)
def parse_grade(grade):
    """ Validate grade value """
    try:
        grade = float(grade)
    except ValueError:
        raise ValueError("Grade must be a number")
    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100")
    return grade
def parse_name(name):
    """ Validate name value"""
    if not name.strip():
        raise ValueError("Name cannot be empty")
    return name.strip()

def parse_student_id(student_id):
    """ Validate student ID"""
    if student_id <= 0:
        raise ValueError("Student ID must be a positive number")
    return student_id


def main():
    """ Argparser commands to use for CLI """
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
    p4.add_argument("--grade", required=True)

    
    p5 = subparsers.add_parser("list")
    p5.add_argument("type", choices=["students", "courses", "enrollments"])

    
    p6 = subparsers.add_parser("avg")
    p6.add_argument("--student-id", required=True, type=int)
    p6.add_argument("--course", required=True)

    
    p7 = subparsers.add_parser("gpa")
    p7.add_argument("--student-id", required=True, type=int)

    args = parser.parse_args()
    data = load_data()

    try:
        if args.command == "add-student":
            name = parse_name(args.name)
            data, new_id = add_student(data, name)
            save_data(data)
            print(f"Student added with ID: {new_id}")

        elif args.command == "add-course":
            if args.code in data["courses"]:
                print(f"Course '{args.code}' already exists")
            else:
                data = add_course(data, args.code, args.title)
                save_data(data)
                print(f"Course '{args.title}' added")
                
        elif args.command == "enroll":
            student_id = parse_student_id(args.student_id)
            if str(student_id) not in data["students"]:
                raise ValueError(f"Student ID {student_id} not found")
            if args.course not in data["courses"]:
                raise ValueError(f"Course '{args.course}' not found")
            data = enroll(data, args.student_id, args.course)
            save_data(data)
            print(f"Student {args.student_id} enrolled in {args.course}!")

        elif args.command == "add-grade":
            student_id = parse_student_id(args.student_id)
            grade = parse_grade(args.grade)
            if str(student_id) not in data["students"]:
                raise ValueError(f"Student ID {student_id} not found")
            if args.course not in data["courses"]:
                raise ValueError(f"Course '{args.course}' not found")
            enrolled = any(
                e for e in data["enrollments"]
                if e["student_id"] == student_id and e["course_code"] == args.course
            )
            if not enrolled:
                raise ValueError(f"Student {student_id} is not enrolled in {args.course}")
            data = add_grade(data, args.student_id, args.course, grade) 
            save_data(data)
            print(f"Grade {args.grade} added")

        elif args.command == "list":
            if args.type == "students":
                for sid, s in list_students(data):
                    print(f"ID: {sid} | Name: {s['name']}")
            elif args.type == "courses":
                for code, c in list_courses(data):
                    print(f"Code: {code} | Title: {c['title']}")
            elif args.type == "enrollments":
                for e in list_enrollments(data):
                    print(f"Student ID: {e['student_id']} | Course: {e['course_code']} | Grades: {e['grades']}")

        elif args.command == "avg":
            student_id = parse_student_id(args.student_id)
            if str(student_id) not in data["students"]:
                raise ValueError(f"Student ID {student_id} not found")
            avg = compute_average(data, args.student_id, args.course)
            print(f"Average grade: {avg:.2f}")

        elif args.command == "gpa":
            student_id = parse_student_id(args.student_id)
            if str(student_id) not in data["students"]:
                raise ValueError(f"Student ID {student_id} not found")
            gpa = compute_gpa(data, args.student_id)
            print(f"GPA: {gpa:.2f}")

        else:
            parser.print_help()
    except ValueError as e:
        print(f"Value Error: {e}")


if __name__ == "__main__":
    main()