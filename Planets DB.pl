% Facts about planets
planet(mercury, rocky, small, 88).
planet(venus, rocky, medium, 225).
planet(earth, rocky, medium, 365).
planet(mars, rocky, small, 687).
planet(jupiter, gas_giant, large, 4333).
planet(saturn, gas_giant, large, 10759).
planet(uranus, ice_giant, medium, 30687).
planet(neptune, ice_giant, medium, 60190).

% Rules for classifying planets
terrestrial(Planet) :- planet(Planet, rocky, _, _).
gas_giant(Planet) :- planet(Planet, gas_giant, _, _).
ice_giant(Planet) :- planet(Planet, ice_giant, _, _).

% Rule to find planets with a specific orbit period
planet_with_orbit_period(Planet, Period) :- planet(Planet, _, _, Period).
