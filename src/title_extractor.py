def extract_title(markdown):
    if not markdown:
        raise Exception("Empty Document!")

    if markdown.startswith("# "):
        title = markdown.strip("# ").split("\n\n")[0]
        if not title:
            raise Exception("Empty Title")

        return title
    else:
        raise Exception("No Title Document Found")
