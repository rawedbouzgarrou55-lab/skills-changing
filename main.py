# skills-changing
class EducationSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students[name] = grade
        print(f"Added {name} with a starting grade of {grade}.")

    def analyze_performance(self):
        avg = sum(self.students.values()) / len(self.students)
        return f"System-wide Average Score: {avg}%"

# Example Usage
if __name__ == "__main__":
    system = EducationSystem()
    system.add_student("Alex", 85)
    system.add_student("Sam", 92)
    print(system.analyze_performance())
