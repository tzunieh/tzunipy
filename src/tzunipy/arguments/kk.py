import os
import argparse


def cli_arguments():
    """Function for defining command line arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'action_type',
        type=str,
        default='',
        choices=[
            'file',
        ],
        help='The type of action you would like to execute'
    )

    parser.add_argument(
        'action',
        type=str,
        default='',
        choices=[
            'rename',
        ],
        help='The type of action you would like to execute'
    )

    parser.add_argument(
        '--dir',
        type=str,
        default=os.getcwd(),
        help='Target directory'
    )

    parser.add_argument(
        '--format',
        type=str,
        default='',
        help='Format'
    )

    parser.add_argument('--dryrun', action='store_true')

    return parser.parse_args()
