-module(solution2).
-export([main/1]).
-export([findword/2]).

main(Args) ->
  [H|T] = Args,
  findword(H, T).

findword(Key, Words) ->
  lists:filter(fun(Desc) -> string:str(Desc, Key) > 0 end, Words).
