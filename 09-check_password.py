def check_password(password: str):
    with open('09-passwords_list.txt','r') as file:
        common_passwords: list[str] = file.read().splitlines()
        #print(common_passwords)

    for i, common_passwords in enumerate(common_passwords, start=1):
         if password == common_passwords:
              print(f'{password}: ❌ found in line (#{i})')
              return
    
    print(f'{password} ✅ (unique)')
         

def main():
        check_password('Luck')

if __name__ == '__main__':
     main()

