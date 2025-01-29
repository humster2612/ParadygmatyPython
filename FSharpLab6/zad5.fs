// znajdujemy najdłuższe słowo w podanym tekście
open System

let findLongestWord (input: string) =

    let words = input.Split([| ' '; '\t'; '\n'; '\r' |], StringSplitOptions.RemoveEmptyEntries)
    let longestWord = words |> Seq.maxBy (fun word -> word.Length)
    longestWord, longestWord.Length

[<EntryPoint>]

let main argv =

    printfn "Wpisz tekst:"

    let userInput = Console.ReadLine()
    let longestWord, length = findLongestWord userInput

    printfn "Najdłuższe słowo: %s (długość: %d)" longestWord length
    0
