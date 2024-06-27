# SAMBA Python
import smbclient

with smbclient.SambaClient(ip, share='Имя шары',
                           username='User', workgroup=wg,
                           port=139, password='123') as client:
    pass
    #client.


