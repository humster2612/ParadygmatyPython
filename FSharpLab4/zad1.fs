open System

type User = {
    Weight : float
    Height : float
    
}

let calculateBMI user =

    user.Weight/(user.Height * user.Height)

let classifyBMI bmi =

    match bmi with
    | x when x  < 18.5 -> "Niedowaga "
    | x when x < 25.0 -> "waga normalna"
    | x when x < 30.0 -> "nadwaga "
    | _ -> "Otyłość"

[<EntryPoint>]
let main argv =
    printfn "Podaj swoją wagę w kilogramach: "

    let weight = Console.ReadLine() |> float
    printfn "Podaj swój wzrost w metrach: "

    let height = Console.ReadLine() |> float

    let user = { Weight = weight; Height = height }
    let bmi = calculateBMI user
    let category = classifyBMI bmi

    printfn "Twoje BMI wynosi %.2f i jest klasyfikowane jako %s" bmi category
    0 
