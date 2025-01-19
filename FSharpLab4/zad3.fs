open System
open System.Linq

let policzSlowa (tekst: string) =

    tekst.Split([| ' '; ','; '.'; ':'; '\t' |], 
    StringSplitOptions.RemoveEmptyEntries).Length

let policzZnaki (tekst: string) =

    tekst.Replace(" ", "").Length

let znajdzNajczestszeSlowo (tekst: string) =

    tekst.ToLower().Split([| ' '; ','; '.'; ':'; '\t' |], 
    StringSplitOptions.RemoveEmptyEntries)


    |> Seq.groupBy id
    |> Seq.map (fun (slowo, wystapienia) -> (slowo, Seq.length wystapienia))
    |> Seq.maxBy snd
    |> fst

[<EntryPoint>]
let main argv =

    printfn "Wprowadź tekst do analizy: "
    let tekst = Console.ReadLine()

    let liczbaSlow = policzSlowa tekst
    let liczbaZnakow = policzZnaki tekst
    let najczestszeSlowo = znajdzNajczestszeSlowo tekst

    printfn "Liczba słów: %d" liczbaSlow
    printfn "Liczba znaków (bez spacji): %d" liczbaZnakow
    printfn "Najczęstsze słowo: %s" najczestszeSlowo
    0
