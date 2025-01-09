def process_results():
    """
    Pobiera dane od użytkownika i zwraca listę wyników w postaci krotek (exam_points, exercises_completed).
    """
    results = []
    while True:
        line = input("Exam points and exercises completed: ")
        if line == "":
            break
        exam_points, exercises_completed = map(int, line.split())
        print(exam_points, exercises_completed)
        results.append((exam_points, exercises_completed))
        print(results)
    return results


def calculate_and_print_statistics(results):
    """
    Oblicza statystyki na podstawie wyników i drukuje je na ekranie.
    """
    total_points = []
    grades = []
    passing_students = 0

    for exam_points, exercises_completed in results:
        exercise_points = exercises_completed // 10  # Punkty za ćwiczenia
        total = exam_points + exercise_points

        # Określanie oceny na podstawie całkowitych punktów
        if exam_points < 10:
            grade = 0
        elif total < 15:
            grade = 0
        elif total <= 17:
            grade = 1
        elif total <= 20:
            grade = 2
        elif total <= 23:
            grade = 3
        elif total <= 27:
            grade = 4
        else:
            grade = 5

        total_points.append(total)
        grades.append(grade)

        if grade > 0:
            passing_students += 1

    # Obliczanie średniej punktów
    points_average = sum(total_points) / len(total_points) if total_points else 0

    # Obliczanie procentu zdających
    pass_percentage = (passing_students / len(results)) * 100 if results else 0

    # Rozkład ocen
    grade_distribution = {i: 0 for i in range(6)}
    for grade in grades:
        grade_distribution[grade] += 1

    # Wyświetlanie wyników
    print("Statistics:")
    print(f"Points average: {points_average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    for grade in range(5, -1, -1):
        stars = "*" * grade_distribution[grade]
        print(f"  {grade}: {stars}")


# Główne wywołanie programu
def main():
    results = process_results()
    calculate_and_print_statistics(results)


main()