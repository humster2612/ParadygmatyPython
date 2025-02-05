type Node<'T> = 
    | Empty
    | Node of 'T * Node<'T>

type LinkedList<'T> =

    { Head : Node<'T> }

let fromList (items: List<'T>) =
    let rec buildList acc items =
    
        match items with
        | [] -> acc
        | head :: tail -> buildList (Node(head, acc)) tail
    { Head = buildList Empty (List.rev items) }
