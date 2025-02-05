let countOccurrences value list =
    let rec countRec count node =
    
        match node with
        | Empty -> count
        | Node(v, next) when v = value -> countRec (count + 1) next
        | Node(_, next) -> countRec count next
    countRec 0 list.Head
