from .arguments.kk import cli_arguments


def main():
    args = cli_arguments()

    if args.action_type == 'file':
        from .handlers import file_handler

        if args.action == 'rename':
            file_handler.rename(args.dir, args.format)

