state(atdoor, onfloor, atwindow, hasnot).
move(state(M, onfloor, B, H), walk(M, M1), state(M1, onfloor, B, H)).
move(state(M, onfloor, M, H), push(M, M1), state(M1, onfloor, M1, H)).
move(state(M, onfloor, M, H), climb, state(M, onbox, M, H)).
move(state(middle, onbox, middle, hasnot), grab, state(middle, onbox, middle, has)).

% Recursive call to find the solution
canget(state(_, _, _, has)).
canget(State1) :-
    move(State1, Move, State2),
    canget(State2),
    write(Move), nl.
