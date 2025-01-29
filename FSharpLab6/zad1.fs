open System

let countWordsAndCharacters (input: string) =
    let words = input.Split([| ' '; '\t'; '\n'; '\r' |], StringSplitOptions.RemoveEmptyEntries)
    let characters = input.Replace(" ", "")
    printfn "Liczba słów: %d" (words.Length)
    printfn "Liczba znaków bez spacji: %d" (characters.Length)

[<EntryPoint>]

let main argv =
    printfn "Wpisz tekst:"
    let userInput = Console.ReadLine()
    countWordsAndCharacters userInput
    0
