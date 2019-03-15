def str_trim(item: str):
    return ' '.join(item.split())


def guess_title(filename: str) -> str:
    if '-' in filename:
        title_side = filename.split('-', maxsplit=1)[1]
        return str_trim(title_side[:-4])
    return filename[:-4]


def guess_artist(filename: str) -> str:
    if '-' in filename:
        return str_trim(filename.split('-', maxsplit=1)[0])
    return ''
