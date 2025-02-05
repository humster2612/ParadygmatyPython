type SearchResult =
    | Found of int
    | NotFound

let indexOf value list =
    let rec indexRec index node =
    
        match node with
        | Empty -> NotFound
        | Node(v, next) when v = value -> Found index
        | Node(_, next) -> indexRec (index + 1) next
    indexRec 0 list.Head
