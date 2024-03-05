sum(0, 0).  % Base case: sum of 0 is 0
sum(N, Result) :-
    N > 0,   % Ensure N is a positive integer
    N1 is N - 1,
    sum(N1, SubResult),
    Result is N + SubResult.

