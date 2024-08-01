import randomSeed
import encrypt

def getRotorNum() -> int:
    while True:
        try:
            rotorNum = int(input("Enter number of rotor for your Encryption"))
            break
        except:
            print('Enter Integer')
    return rotorNum

def getSeed(n: int) -> list:
    m = 0
    seed_list = [0 in range(n)]
    while n > m:
        try:
            seedNum = int(input("Enter Seed for your Encryption"))
            seed_list[m] = seedNum
            m += 1
        except:
            print('Enter Integer')
    return seed_list

def main():
    message: str = input('Enter Data for Encryption')

    # making dynamic variable using dictionary
    make_var: int = 0
    rotor_number = getRotorNum() #number of rotor used for encryption
    seed_list = getSeed(rotor_number) #number of seed user input
    rotor_dict = {}
    while make_var < rotor_number:
        key: int= make_var
        val: list = randomSeed.rotor(seed_list[make_var])
        make_var += 1
        rotor_dict[key]= val
    print(rotor_dict)

    # encrypting message
    result = encrypt.encrypt(message, rotor_dict)

    #result
    print(result)

if __name__ == '__main__':
    main()