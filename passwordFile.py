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
    print('Press 1 to add password for this account or 0 to exit')
    rep=int(input())
    if rep == 0:
        sys.exit()
    elif rep == 1:
        print('Enter the password for '+account+':')
        pwds[account]=input()
        print('Password has been stored.')
