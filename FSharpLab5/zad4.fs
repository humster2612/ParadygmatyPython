// to funkcja rkurencyjna 
let rec whanoi n source aux target =
    match n with
    | 0 -> []
    | _ ->
    
        whanoi (n - 1) source target aux @
        [(source, target)] @
        whanoi (n - 1) aux source target

//  to funkcja iteracyjna 


// let hanoiIter n =
//     let moves = System.Collections.Generic.List<_,_>()
//     moves
