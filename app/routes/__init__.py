def get_arg(args, arg_name, default=None):
    return args.get(arg_name, default) if args else default


def get_pagination_args(args):
    try:
        page = int(get_arg(args, "page", 1))
        per_page = int(get_arg(args, "per_page", 10))
    except ValueError:
        page = 1
        per_page = 10
    return page, per_page
