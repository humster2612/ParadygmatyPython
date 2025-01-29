let rec permute list =

    match list with
    | [] -> [[]]
    | x :: xs ->
        [for perms in permute xs do
            for i in [0 .. List.length perms] do
                yield List.insertAt i x perms]
