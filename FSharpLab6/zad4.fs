open System

let zmianaFormat (input: string) =
    let entries = input.Split(';')

    if entries.Length = 3 then
        let name = entries.[0].Trim()
        let surname = entries.[1].Trim()
        let age = entries.[2].Trim()

        sprintf "%s, %s (%s lat)" surname name age
    else
        "Nieprawidłowe dane"

[<EntryPoint>]

let main argv =

    printfn "Wprowadź dane w formacie 'imię; nazwisko; wiek':"

    let userData = Console.ReadLine()
    let result = zmianaFormat userData

    printfn "%s" result
    0
