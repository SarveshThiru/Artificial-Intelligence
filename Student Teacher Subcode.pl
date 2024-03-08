teacher(mr_smith).
teacher(ms_jones).
teacher(dr_brown).

student(john).
student(lisa).
student(bob).

subject(math).
subject(english).
subject(physics).

% Relationships
teaches(mr_smith, math, 'MATH101').
teaches(ms_jones, english, 'ENG201').
teaches(dr_brown, physics, 'PHY301').

enrolled(john, math).
enrolled(john, english).
enrolled(lisa, english).
enrolled(bob, physics).

% Rules
student_subject_code(Student, Subject, Code) :-
    enrolled(Student, Subject),
    teaches(Teacher, Subject, Code).
