import os
BLUE = "\033[1;34m"
os.system("clear")
banner1 ="""
     _   _           _     
    | | | |         | |    
    | |_| | __ _ ___| |__  
    |  _  |/ _` / __| '_ \ 
    | | | | (_| \__ \ | | |
    \_| |_/\__,_|___/_| |_|
    
"""
banner2 = """
         _____    _            _   _  __ _           
        |_   _|  | |          | | (_)/ _(_)          
          | |  __| | ___ _ __ | |_ _| |_ _  ___ _ __ 
          | | / _` |/ _ \ '_ \| __| |  _| |/ _ \ '__|
         _| || (_| |  __/ | | | |_| | | | |  __/ |   
         \___/\__,_|\___|_| |_|\__|_|_| |_|\___|_|   
         """
def banner():
	print(BLUE+"#"*64)
	print(banner1,banner2)
	print("\nCreated by Safin Mohammad")
	print()
	print("#"*64)
banner()
print("Avlable hashes ")
print("[+] CRC16 ")
print("[+] MD5  ")
print("[+] SHA-1 ")
print("[+] SHA-224 ")
print("[+] SHA-256")
print("[+] SHA-384")
print("[+] SHA-512")
hash = input("[+] Enter Your hash : ")
if len(hash) <= 3:
	print("[!] Invalid hash")
elif len(hash) == 4:
    print("[+] CRC16  hash")
elif len(hash) == 32:
    print("[+] MD5 hash")    
elif len(hash) == 40:
    print("[+] SHA-1 hash")   
elif len(hash) == 56:
    print("[+] SHA-224 hash")    
elif len(hash) == 64:
    print("[+] SHA-256 hash")    
elif len(hash) == 96:
    print("[+] SHA-384 hash")   
elif len(hash) == 128:
    print("[+] SHA-512 hash")    
else:
	print("[-] Unknown hash")
