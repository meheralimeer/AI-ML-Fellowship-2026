"""Student Record System | Dictionaries, Lists, Comprehensions"""

class StudentRecordSystem:
    def __init__(self):
        self.students = {}
    
    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print(f"Student ID '{student_id}' already exists")
            return False
        
        self.students[student_id] = {
            "name": name,
            "age": age,
            "grade": grade,
            "scores": {}
        }
        return True
    
    def add_score(self, student_id, subject, score):
        if student_id not in self.students:
            return False
        self.students[student_id]["scores"][subject] = score
        return True
    
    def add_multiple_scores(self, student_id, **scores):
        if student_id not in self.students:
            return False
        self.students[student_id]["scores"].update(scores)
        return True
    
    def update_student(self, student_id, **fields):
        if student_id not in self.students:
            return False
        for field, value in fields.items():
            if field in ["name", "age", "grade"]:
                self.students[student_id][field] = value
        return True
    
    def calculate_average(self, student_id):
        if student_id not in self.students:
            return None
        scores = self.students[student_id]["scores"]
        if not scores:
            return None
        return sum(scores.values()) / len(scores)
    
    def get_grade_letter(self, average):
        if average >= 90: return 'A'
        elif average >= 80: return 'B'
        elif average >= 70: return 'C'
        elif average >= 60: return 'D'
        else: return 'F'
    
    def display_student(self, student_id):
        if student_id not in self.students:
            return
        
        student = self.students[student_id]
        average = self.calculate_average(student_id)
        
        print(f"\n=== {student['name']} ===")
        print(f"ID: {student_id}")
        print(f"Age: {student['age']}, Grade: {student['grade']}")
        print("Scores:")
        for subject, score in student['scores'].items():
            print(f"  {subject}: {score}")
        if average:
            print(f"Average: {average:.2f} ({self.get_grade_letter(average)})")
    
    def get_top_students(self, n=5):
        student_averages = {
            sid: self.calculate_average(sid)
            for sid in self.students
            if self.calculate_average(sid) is not None
        }
        
        top_ids = sorted(student_averages.keys(), 
                        key=lambda x: student_averages[x], 
                        reverse=True)[:n]
        
        return [
            {
                "id": sid,
                "name": self.students[sid]["name"],
                "average": student_averages[sid]
            }
            for sid in top_ids
        ]
    
    def get_students_by_grade(self, min_average):
        return [
            {
                "id": sid,
                "name": student["name"],
                "average": self.calculate_average(sid)
            }
            for sid, student in self.students.items()
            if self.calculate_average(sid) and self.calculate_average(sid) >= min_average
        ]

if __name__ == "__main__":
    system = StudentRecordSystem()
    
    system.add_student("S001", "Alice Johnson", 18, "12th")
    system.add_student("S002", "Bob Smith", 17, "11th")
    system.add_student("S003", "Charlie Brown", 18, "12th")
    
    system.add_multiple_scores("01", Math=95, Science=92, English=88)
    system.add_multiple_scores("02", Math=78, Science=82, English=85)
    system.add_multiple_scores("03", Math=88, Science=85, English=90)
    
    system.display_student("S001")
    
    print("\nTop Students =-")
    for student in system.get_top_students(3):
        print(f"{student['name']}: {student['average']:.2f}")
    
    print("\nHigh Performers (avg >= 85) =-")
    for student in system.get_students_by_grade(85):
        print(f"{student['name']}: {student['average']:.2f}")
