let partition predicate list =
    let rec partitionRec node yesAcc noAcc =
    
        match node with
        | Empty -> ({ Head = reverse yesAcc Empty }, { Head = reverse noAcc Empty })
        | Node(value, next) when predicate value ->
            partitionRec next (Node(value, yesAcc)) noAcc
        | Node(value, next) ->
            partitionRec next yesAcc (Node(value, noAcc))
    partitionRec list.Head Empty Empty


