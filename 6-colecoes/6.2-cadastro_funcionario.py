# Criando dicionário composto de cadastro de funcionário
funcionarios = {
    "44356":{
            "nome":"Vitor Davi",
            "telefone":"11912121315",
            "data_nascimento":"26/03/2010",
            "cargo":"Jovem Aprendiz",
            "habilidades":["front-end","java","python"]
    },
    "42568":{
            "nome":"Adriano Barros",
            "telefone":"11940404040",
            "data_nascimento":"24/03/2010",
            "cargo":"Jovem Aprendiz",
            "habilidades":["front-end","java","python"]

    },
    "41548":{
            "nome":"Mimi Cristine",
            "telefone":"11970707070",
            "data_nascimento":"15/09/2010",
            "cargo":"Jovem Aprendiz",
            "habilidades":["Pacote","python"]
    
    }

}

print(funcionarios["44356"]["habilidades"][1])