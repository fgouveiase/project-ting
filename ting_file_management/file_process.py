import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for i in range(len(instance)):
        name = instance.search(i)
        if name["nome_do_arquivo"] == path_file:
            return None

    lines = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(result)

    print(result)


def remove(instance):
    """Aqui irá sua implementação"""
    if not len(instance):
        print("Não há elementos")
        return
    removed = instance.dequeue()
    print(f'Arquivo {removed["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        print(instance.search(position))
    except Exception:
        print("Posição inválida", file=sys.stderr)
