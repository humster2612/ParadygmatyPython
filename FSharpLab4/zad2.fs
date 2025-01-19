open System
open System.Collections.Generic

let kursyWymiany = dict [

    ("USD", "EUR", 0.91)
    ("EUR", "USD", 1.10)
    ("GBP", "USD", 1.23)
    ("USD", "GBP", 0.81)
    ("EUR", "GBP", 0.89)
    ("GBP", "EUR", 1.12)

]

let przeliczWalute kwota walutaZrodlowa walutaDocelowa =

    let kurs = kursyWymiany.[(walutaZrodlowa, walutaDocelowa)]
    kwota * kurs

[<EntryPoint>]

let main argv =

    printfn "Wprowadź kwotę do przeliczenia: "
    let kwota = Console.ReadLine() |> float

    printfn "Wprowadź walutę źródłową: "
    let walutaZrodlowa = Console.ReadLine()

    printfn "Wprowadź walutę docelową: "
    let walutaDocelowa = Console.ReadLine()

    let przeliczonaKwota = przeliczWalute kwota walutaZrodlowa walutaDocelowa
    
    printfn "Przeliczona kwota: %.2f %s" przeliczonaKwota walutaDocelowa
    0
