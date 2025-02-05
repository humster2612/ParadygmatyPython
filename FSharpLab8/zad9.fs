let compareLists list1 list2 =
    let rec compare l1 l2 acc =
    
        match (l1, l2) with
        | (Node(v1, n1), Node(v2, n2)) -> compare n1 n2 ((v1 > v2) :: acc)
        | (Empty, Empty) -> List.rev acc
        | _ -> failwith "Lists are of different lengths"
    compare list1.Head list2.Head []
