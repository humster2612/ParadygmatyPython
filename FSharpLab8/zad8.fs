let concat list1 list2 =
    let rec reverse node acc =
    
        match node with
        | Empty -> acc
        | Node(value, next) -> reverse next (Node(value, acc))

    let rec connect l1 l2 =

        match l1 with
        | Empty -> l2
        | Node(value, next) -> connect next (Node(value, l2))
    { Head = connect (reverse list1.Head Empty) list2.Head }
