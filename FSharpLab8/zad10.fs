let filterList predicate list =
    let rec filterRec node acc =
    
        match node with
        | Empty -> { Head = acc }
        | Node(value, next) when predicate value -> filterRec next (Node(value, acc))
        | Node(_, next) -> filterRec next acc
    filterRec (reverse list.Head Empty) Empty
