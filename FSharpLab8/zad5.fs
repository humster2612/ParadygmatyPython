let contains value list =
    let rec containsRec node =
    
        match node with
        | Empty -> false
        | Node(v, next) when v = value -> true
        | Node(_, next) -> containsRec next
    containsRec list.Head

