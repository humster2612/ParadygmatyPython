open System

let isPalindrome (input: string) =
    let reversed = new string(Array.rev (input.ToCharArray()))
    input = reversed


[<EntryPoint>]


let main argv =

    printfn "Podaj tekst do sprawdzenia:"

    let text = Console.ReadLine()

    if isPalindrome text then
        printfn "Tekst jest palindromem"
    else
        printfn "Tekst nie jest palindromem"
    0
