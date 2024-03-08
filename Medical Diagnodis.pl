% Facts
symptom(patient, cough).
symptom(patient, fever).
symptom(patient, runny_nose).
symptom(patient, headache).

% Rules
disease(Disease) :-
    symptom(patient, Symptom1),
    symptom(patient, Symptom2),
    symptom(patient, Symptom3),
    disease_symptoms(Disease, Symptom1, Symptom2, Symptom3).

% Diseases and their symptoms
disease_symptoms(flu, fever, cough, runny_nose).
disease_symptoms(common_cold, cough, runny_nose, headache).
disease_symptoms(meningitis, fever, headache, stiff_neck).
