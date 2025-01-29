let fibTail n =
    let rec fibAux n a b =
        match n with
        | 0 -> a
        | _ -> fibAux (n - 1) b (a + b)
    fibAux n 0 1
