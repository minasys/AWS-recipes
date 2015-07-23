#!/usr/bin/env python2

# Import AWS utils
from AWSUtils.utils import *
from AWSUtils.utils_iam import *
from AWSUtils.utils_sts import *

# Import third-party modules
import sys

########################################
##### Main
########################################

def main(args):

    # Configure the debug level
    configPrintException(args.debug)

    # Init STS session
    try:
        init_sts_session_and_save_in_credentials(args.profile[0], mfa_code = args.mfa_code[0], mfa_serial_arg = args.mfa_serial[0])
    except Exception, e:
        printException(e)
        return 42


########################################
##### Parse arguments and call main()
########################################

add_sts_argument(parser, 'mfa_serial')
add_sts_argument(parser, 'mfa_code')

args = parser.parse_args()

if __name__ == '__main__':
    sys.exit(main(args))
