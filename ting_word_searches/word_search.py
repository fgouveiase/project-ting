def exists_word(word, instance):
    result = []

    for i in range(len(instance)):
        file = instance.search(i)
        lines = file["linhas_do_arquivo"]

        ocurrences = [
            {"linha": i + 1}
            for index in range(len(lines))
            if word.lower() in lines[index].lower()
        ]

    if len(ocurrences) > 0:
        search_result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": ocurrences,
        }
        result.append(search_result)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
