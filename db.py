file_name = "estoque.txt"


def write_albuns(name, quanty, preco , gelado):
    with open(file_name, "a", encoding="UTF-8") as file:
        file.write(f"{name}|{quanty}|{preco}|{gelado}\n")
#teste

def read_albuns():
    produtos = []
    with open(file_name, "r", encoding="UTF-8") as file:
        lines = file.read().split("\n")
        for line in lines:
            if line:
                produtos.append(line)
    return produtos

