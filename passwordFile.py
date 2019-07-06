#! python3

#A password storage file which copies the corresponding password to the clipboard.

import sys
import pyperclip

pwds={
    'email':'sri123',
    'blog':'abcde',
    'instagram':'1234'
}

if len(sys.argv)<2:
    print('Usage:passwordFile.py [account] - Your account password will be copied to clipboard')
    sys.exit()
account=sys.argv[1]

if account in pwds:
    pyperclip.copy(pwds[account])
    print('Password for '+account+' has been copied to clipboard.')
else:
    print('Password for '+account+' does not exist.')
