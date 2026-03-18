from homework import Homework
from exam import Exam
from grade import ExamG
from weak_grade import ExamH

print("--- Homework ---")
g = Homework()
g.grade = 93
assert g.grade >= 90  # jesli nie spełnia warunky rzuca error
print(f"Ocena za projekt: {g.grade}")
# --- Homework ---
# Ocena za projekt: 93


print("--- Exam ---")
ex = Exam()
ex.part_a_grade = 88
ex.part_b_grade = 67

assert ex.part_a_grade >= 80
assert ex.part_b_grade >= 55

print(f"Ocena całościowa: a -> {ex.part_a_grade}, B -> {ex.part_b_grade}")
# --- Exam ---
# Ocena całościowa: a -> 88, B -> 67

print("--- ExamG ---")
first = ExamG()
first.math_grade = 34
first.alg_grade = 13
first.prog_grade = 55

print("Termin I")
print(first.math_grade, first.alg_grade, first.prog_grade)
# --- ExamG ---
# Termin I
# 34 13 55

sec = ExamG()
sec.math_grade = 53
sec.alg_grade = 73
sec.prog_grade = 89

print("Termin II")
print(sec.math_grade, sec.alg_grade, sec.prog_grade)
# Termin II
# 53 73 89

print('Archiwum (ExamG) TERMIN I')
print(first.math_grade, first.alg_grade, first.prog_grade)
# Archiwum (ExamG) TERMIN I
# 53 73 89 - to nie jest TERMIN I


print(70 * "-")
print("--- ExamH ---")
first = ExamH()
first.math_grade = 34
first.alg_grade = 13
first.prog_grade = 55

print("Termin I")
print(first.math_grade, first.alg_grade, first.prog_grade)
# --- ExamG ---
# Termin I
# 34 13 55

sec = ExamH()
sec.math_grade = 53
sec.alg_grade = 73
sec.prog_grade = 89

print("Termin II")
print(sec.math_grade, sec.alg_grade, sec.prog_grade)
# Termin II
# 53 73 89
# ----------------------------------------------------------------------
# --- ExamH ---
# Termin I
# 34 13 55
# Termin II
# 53 73 89
print('Archiwum TERMIN I')
print(first.math_grade, first.alg_grade, first.prog_grade)
# Archiwum TERMIN I
# 34 13 55
