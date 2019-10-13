#! python3

#A password storage file which copies the corresponding password to the clipboard.

import sys
import pyperclip

pwdFile = open('passwords.txt')
pwds='{'+pwdFile.read()+'}'
pwds=eval(pwds)
if len(sys.argv)<2:
    print('Usage:passwordFile.py [account] - Your account password will be copied to clipboard')
    sys.exit()
account=sys.argv[1]

if account in pwds:
    pyperclip.copy(pwds[account])
    print('Password for '+account+' has been copied to clipboard.')
    pwdFile.close()
else:
    pwdFile.close()
    print('Password for '+account+' does not exist.')
    rep=int(input('Press 1 to add password for this account or 0 to exit: '))
    if rep == 0:
        sys.exit()
    elif rep == 1:
        pwdFile=open('passwords.txt', 'a')
        newPwd=input('Enter the password for '+account+':')
        pwdFile.write(",'%s':'%s'"%(account,newPwd))
        print('Password has been stored.')
        pwdFile.close()
