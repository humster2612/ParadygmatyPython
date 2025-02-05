let reverse list =
    let rec reverseAcc node acc =
    
        match node with
        | Empty -> acc
        | Node(value, next) -> reverseAcc (next) (Node(value, acc))
    { Head = reverseAcc list.Head Empty }
