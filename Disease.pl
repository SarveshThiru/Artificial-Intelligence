% Define diseases and recommended diets
disease(diabetes).
disease(heart_disease).
disease(hypertension).

diet(low_sugar).
diet(low_sodium).
diet(low_cholesterol).

% Define the relationship between diseases and diets
recommended_diet(diabetes, low_sugar).
recommended_diet(heart_disease, low_cholesterol).
recommended_diet(hypertension, low_sodium).

% Define the rule
suggest_diet(Disease, Diet) :-
    disease(Disease),
    diet(Diet),
    recommended_diet(Disease, Diet).
