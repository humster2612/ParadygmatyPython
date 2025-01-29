open System

let removeDuplicates (input: string) =

    let words = input.Split([| ' ' |], StringSplitOptions.RemoveEmptyEntries)
    words |> Seq.distinct |> Seq.toList

[<EntryPoint>]


let main argv =
   
    printfn "Podaj słowa oddzielone spacjami:"


    let userInput = Console.ReadLine()
    let uniqueWords = removeDuplicates userInput
    
    printfn "Unikalne słowa: %A" uniqueWords
    0
