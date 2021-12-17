# Вывести фамилию, имя студента, оценки по предметам за 1 семестр из зачётной книжки.
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def mark(student, **scores):
    print(f"Student's Name and Surname: {student}.")
    for subjects, score in scores.items():
        sorted(subjects)
        print(f"{subjects}: {score}.")


if __name__ == '__main__':
    mark(
        "Горлов Дмитрий",
        Jurisprudence="Хорошо", Information_Technology_in_Telecommunications="Отлично",
        Physical_Basics_of_Telecommunications="Хорошо", Philosophy="Отлично", Russian_language="Отлично",
        English_language="Хорошо", Russian_History="Отлично", Physical_Education="Отлично",
        Elective_Classes_of_PE="Отлично", Introduction_to_Web_Technologies="Зачтено",
        Crossplatform_Programming_Basics="Зачтено"
    )
