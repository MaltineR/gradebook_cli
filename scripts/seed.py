from gradebook.storage import save_data

data = {
    "students": {
        "1": {"name": "Maltine"},
        "2": {"name": "Mirgete"},
        "3": {"name": "Erdite"}
    },
    "courses": {
        "OS101": {"title": "Operating Systems"},
        "DS101": {"title": "Data Structures"},
        "ST101": {"title": "Software Testing"}
    },
    "enrollments": [
        {"student_id": 1, "course_code": "OS101", "grades": [90, 85, 92]},
        {"student_id": 1, "course_code": "DS101", "grades": [78, 88]},
        {"student_id": 2, "course_code": "DS101", "grades": [70, 75]},
        {"student_id": 2, "course_code": "ST101", "grades": [80, 90]},
        {"student_id": 3, "course_code": "OS101", "grades": [95, 100]},
        {"student_id": 3, "course_code": "ST101", "grades": [88, 92]}
    ]
}

save_data(data)
print("Data created successfully")