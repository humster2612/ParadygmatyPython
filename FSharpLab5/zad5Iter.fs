// QuickSort iteracyjny

let quicksortIter list =
    let stack = System.Collections.Generic.Stack<List<_>>()

    stack.Push(list)
    let mutable sorted = []

    while stack.Count > 0 do
        match stack.Pop() with
        | [] -> ()
        | x :: xs ->

            let smaller, greater = List.partition (fun y -> y < x) xs
            stack.Push(greater)
            stack.Push(smaller)
            
            sorted <- x :: sorted
    List.rev sorted
