#!c:\users\administrator\code\python\learning_log\ll_env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'shadowsocks==2.8.2','console_scripts','sslocal'
__requires__ = 'shadowsocks==2.8.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('shadowsocks==2.8.2', 'console_scripts', 'sslocal')()
    )
