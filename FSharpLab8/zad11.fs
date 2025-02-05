let removeDuplicates list =
    let rec remove node seen acc =
    
        match node with
        | Empty -> { Head = reverse acc Empty }
        | Node(value, next) when Set.contains value seen ->
            remove next seen acc
        | Node(value, next) ->
            remove next (Set.add value seen) (Node(value, acc))
    { Head = remove list.Head Set.empty Empty }
