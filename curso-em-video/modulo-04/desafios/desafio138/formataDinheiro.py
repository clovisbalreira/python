def formataDinheiro(valor:float):
    import locale
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    return locale.currency(valor, grouping=True)