// QuickSort rekurencyjny 

let rec quicksort list =

    match list with
    | [] -> []
    | x :: xs ->

        let smaller, greater = List.partition (fun y -> y < x) xs
        quicksort smaller @ [x] @ quicksort greater


