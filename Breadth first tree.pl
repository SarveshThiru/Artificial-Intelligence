% Facts
edge(a, b).
edge(b, c).
edge(c, d).
edge(d, e).
edge(a, e).

% Rules
path(Start, End, Path) :-
    bfs([[Start]], End, ReversedPath),
    reverse(ReversedPath, Path).

bfs([[Node|Path]|_], End, [Node|Path]) :-
    Node == End.

bfs([[Node|Path]|Paths], End, Result) :-
    findall(X, (edge(Node, X), \+ member(X, [Node|Path])), Nodes),
    add_to_paths(Nodes, [Node|Path], NewPaths),
    append(Paths, NewPaths, UpdatedPaths),
    bfs(UpdatedPaths, End, Result).

add_to_paths([], _, []).
add_to_paths([Node|Nodes], Path, [[Node|Path]|Paths]) :-
    add_to_paths(Nodes, Path, Paths).

% Query
% ?- path(a, d, Path).
