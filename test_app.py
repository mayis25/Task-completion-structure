from app import read_students, find_student

def test_read_students():
    """Тест чтения студентов"""
    students = read_students('students.md')
    assert len(students) > 0

def test_find_student():
    """Тест поиска студента"""
    test_students = [
        {
            'full_name': 'Иванов Иван Иванович',
            'group': 'ТВ-101',
            'college': 'Технический колледж',
            'admission_year': 2023,
            'course': 2
        }
    ]
    
    student = find_student(test_students, 'Иванов Иван Иванович')
    assert student is not None
    assert student['group'] == 'ТВ-101'