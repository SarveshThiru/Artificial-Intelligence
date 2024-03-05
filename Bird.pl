bird(canary).
bird(penguin).
bird(ostrich).
bird(crow).
bird(tocatoucan).
bird(eagle).

can_fly(canary).
can_fly(crow).
can_fly(pegion).
can_fly(tocatoucan).
can_fly(eagle).

bird_can_fly(Bird) :-
    bird(Bird),
    can_fly(Bird).
