//  Rekurencyjna 

type BinaryNode<'T> = 
    | Node of 'T * BinaryNode<'T> * BinaryNode<'T>
    | Empty

let rec findRecursive item tree =
    match tree with
    | Empty -> false
    | Node(value, left, right) ->
        if item = value then true
        else findRecursive item left || findRecursive item right

// Iteracyjna 
// let findIterative item tree =
//     let mutable stack = [tree]
//     while stack <> [] do
//         match stack with
//         | Empty :: t -> stack <- t
//         | Node(value, left, right) :: t ->
//             if item = value then return true
//             stack <- left :: right :: t
//     false
