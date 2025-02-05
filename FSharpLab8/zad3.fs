let findMinMax list =
    let rec find mm node =

        match node with
        | Empty -> mm
        | Node(value, next) ->

            let (currentMin, currentMax) = mm
            find (min value currentMin, max value currentMax) next
            
    match list.Head with
    | Empty -> None
    | Node(value, next) -> Some (find (value, value) next)
