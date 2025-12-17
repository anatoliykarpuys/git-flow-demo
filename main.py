# main.py
import auth

def main():
    print("Демонстрация системы Git Flow")
    
    # Демонстрация работы функции логина
    result = auth.login("admin", "12345")
    print(result)
    
    result2 = auth.login("user", "111")
    print(result2)

if __name__ == "__main__":
    main()
