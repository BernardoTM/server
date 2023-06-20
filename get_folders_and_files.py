import os


def list_dir(requested_path: str):
    file = open("folders_and_files/index.html", "r", encoding="utf-8")
    folders_and_files = []
    # if os.path.exists(requested_path):
    for item in os.listdir(requested_path):
        if os.path.isdir(requested_path + "/" + item):
            folders_and_files.append(pasta(item, requested_path + "/" + item))
        else:
            if item.endswith(".txt"):
                folders_and_files.append(txt(item, requested_path + "/" + item))
            elif item.endswith(".pdf"):
                folders_and_files.append(pdf(item, requested_path + "/" + item))
            elif item.endswith(".css"):
                folders_and_files.append(css(item, requested_path + "/" + item))
            elif item.endswith(".html"):
                folders_and_files.append(html(item, requested_path + "/" + item))
            elif item.endswith(".py"):
                folders_and_files.append(python(item, requested_path + "/" + item))
            elif (
                item.endswith(".png") or item.endswith(".jpg") or item.endswith(".jpeg")
            ):
                folders_and_files.append(img(item, requested_path + "/" + item))
            else:
                folders_and_files.append(generico(item, requested_path + "/" + item))

    folders_and_files = "".join(folders_and_files)
    file = file.read()

    return file.replace("conteudo", folders_and_files)


def read_file_str(requested_path: str):
    try:
        return (
            open(requested_path, "r", encoding="utf-8").read(),
            "HTTP/1.1 200 OK\r\n\r\n",
        )
    except FileNotFoundError:
        return (
            open("not_found.html", "r", encoding="utf-8"),
            "HTTP/1.1 404 NOT FOUND\r\n\r\n",
        )


def read_file(requested_path: str):
    try:
        return (open(requested_path, "rb").read(), "HTTP/1.1 200 OK\r\n\r\n")

    except FileNotFoundError:
        return (
            open("not_found.html", "r", encoding="utf-8"),
            "HTTP/1.1 404 NOT FOUND\r\n\r\n",
        )


def pdf(name: str, path: str):
    pdf = f"""
        <div class="items">
            <a href="{path}">
                <img src="/img/pdf.png" alt="Arquivo pdf">
                <p> {name} </p>
            </a>
        </div>"""
    return pdf


def img(name: str, path: str):
    img = f"""
        <div class="items">
            <a href="{path}">
                <img src="/img/img.png" alt="Imagem">
                <p> {name} </p>
            </a>
        </div>"""
    return img


def pasta(name: str, path: str):
    pasta = f"""
        <div class="items">
            <a href="{path}">
                <img src="/img/pasta.png" alt="Pasta">
                <p> {name} </p>
            </a>
        </div>"""
    return pasta


def txt(name: str, path: str):
    txt = f"""
        <div class="items">
            <a href="{path}">
                <img src="/img/txt.png" alt="">
                <p> {name} </p>
            </a>
        </div>"""
    return txt


def generico(name: str, path: str):
    generico = f"""
        <div class="items">
            <a href="{path}">
                <img src="/img/generico.jpg" alt="">
                <p> {name} </p>
            </a>
        </div>"""
    return generico


def html(name: str, path: str):
    html = f"""
        <div class="items">
            <a href="{path}">
                <img src="/img/html.png" alt="">
                <p> {name} </p>
            </a>
        </div>"""
    return html


def python(name: str, path: str):
    python = f"""
        <div class="items">
            <a href="{path}">
                <img src="/img/python.png" alt="">
                <p> {name} </p>
            </a>
        </div>"""
    return python


def css(name: str, path: str):
    css = f"""
        <div class="items">
            <a href="{path}">
                <img src="/img/css.png" alt="">
                <p> {name} </p>
            </a>
        </div>"""
    return css
