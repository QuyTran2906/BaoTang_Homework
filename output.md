# BaoTang_Homework
***Định dạng request:***

{
    "students": [
        {
            "student_id": "SV001",
            "name": "Nguyen Anh Tu",
            "age": 21,
            "gender": "male"
        },
        {
            "student_id": "SV002",
            "name": "Le Minh Thu",
            "age": 23,
            "gender": "female"
        },
        {
            "student_id": "SV001",
            "name": "Nguyen Anh Tu",
            "age": 21,
            "gender": "male"
        },
        {
            "student_id": "SV001",
            "name": "Nguyen Anh Tu",
            "age": 21,
            "gender": "male"
        },
        {
            "student_id": "SV003",
            "name": "Pham Quoc Viet",
            "age": 20,
            "gender": "male"
        }
    ]
}

***Định dạng response:****
nếu thành công:
{
    "duplicate_students": [
        {
            "age": 21,
            "gender": "male",
            "name": "Nguyen Anh Tu",
            "student_id": "SV001"
        },
        {
            "age": 21,
            "gender": "male",
            "name": "Nguyen Anh Tu",
            "student_id": "SV001"
        }
    ],
    "message": "The list has been processed successfully",
    "status": "success",
    "student_eligible_for_free_ticket": [
        {
            "age": 21,
            "gender": "male",
            "name": "Nguyen Anh Tu",
            "student_id": "SV001"
        },
        {
            "age": 20,
            "gender": "male",
            "name": "Pham Quoc Viet",
            "student_id": "SV003"
        }
    ],
    "total_students": 2
}


nếu không thành công (trường hợp sai gender):
{
    "message": "Gender must be \"male\" or \"female\"",
    "status": "error"
}
