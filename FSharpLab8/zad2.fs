let sum list =
    let rec sumAcc node acc =
    
        match node with
        | Empty -> acc
        | Node(value, next) -> sumAcc (next) (acc + value)
    sumAcc list.Head 0
