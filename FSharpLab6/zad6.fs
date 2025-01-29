open System

let searchAndReplace (text: string) (searchWord: string) (replacementWord: string) =
    text.Replace(searchWord, replacementWord)

[<EntryPoint>]


let main argv =
   
    printfn "Wpisz tekst:"
    let text = Console.ReadLine()
   
    printfn "Podaj słowo do wyszukiwania:"
    let searchWord = Console.ReadLine()
   
    printfn "Podaj słowo na zamianę:"
   
    let replacementWord = Console.ReadLine()
    let newText = searchAndReplace text searchWord replacementWord
   
    printfn "Zmodyfikowany tekst: %s" newText
    0
