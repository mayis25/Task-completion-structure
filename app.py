def read_students(filename):
    """Читаем список студентов из файла"""
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Пропускаем первые 3 строки (заголовки)
        for line in lines[3:]:
            if '|' in line and line.strip():
                parts = line.split('|')
                if len(parts) >= 6:
                    student = {
                        'full_name': parts[1].strip(),
                        'group': parts[2].strip(),
                        'college': parts[3].strip(),
                        'admission_year': int(parts[4].strip()),
                        'course': int(parts[5].strip())
                    }
                    students.append(student)
                    
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
    return students

def find_student(students, name):
    """Ищем студента по имени"""
    for student in students:
        if student['full_name'].lower() == name.lower():
            return student
    return None

def show_student_info(student):
    """Показываем информацию о студенте"""
    print(f"\n🎓 Привет, {student['full_name']}!")
    print("=" * 40)
    print(f"🏫 Колледж: {student['college']}")
    print(f"👥 Группа: {student['group']}")
    print(f"📅 Год поступления: {student['admission_year']}")
    print(f"📚 Курс: {student['course']}")

def main():
    """Главная функция программы"""
    students = read_students('students.md')
    
    print("🎓 Система поиска студентов")
    print("=" * 30)
    
    while True:
        name = input("\nВведите ФИО студента (или 'выход' для завершения): ")
        
        if name.lower() == 'выход':
            print("До свидания!")
            break
            
        student = find_student(students, name)
        
        if student:
            show_student_info(student)
        else:
            print(f"❌ Студент {name} не найден")

if __name__ == "__main__":
    main()