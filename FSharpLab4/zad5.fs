open System

let board = Array.create 9 " "

let printBoard () =
    printfn "\n %s | %s | %s " board.[0] board.[1] board.[2]
    printfn "---+---+---"
    printfn " %s | %s | %s " board.[3] board.[4] board.[5]
    printfn "---+---+---"
    printfn " %s | %s | %s \n" board.[6] board.[7] board.[8]

let checkWin () =

    let lines = [(0,1,2); (3,4,5); (6,7,8); (0,3,6); (1,4,7); (2,5,8); (0,4,8); (2,4,6)]
    lines |> List.exists (fun (a, b, c) -> 

        if board.[a] <> " " && board.[a] = board.[b] && board.[b] = board.[c] then

            printfn "Wygrał %s!" board.[a]
            true
        else false)

let makeMove (player : string) =

    let mutable valid = false
    while not valid do

        printf "Ruch gracza %s (0-8): " player
        let input = Console.ReadLine()

        if Int32.TryParse(input, &_) && input.Length = 1 && board.[int input].[0] = ' ' then
            board.[int input] <- player
            valid <- true
        else
            printfn "Niepoprawny ruch, spróbuj ponownie."

let gameLoop () =

    let mutable turn = 0
    while not (checkWin() || turn = 9) do
        printBoard()
        
        if turn % 2 = 0 then
            makeMove "X"
        else
            makeMove "O"
        turn <- turn + 1


    if turn = 9 && not (checkWin()) then

        printfn "Remis!"


[<EntryPoint>]

let main argv =
    gameLoop()
    0
