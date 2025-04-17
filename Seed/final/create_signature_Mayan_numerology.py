import random
import os

mayan_seals = [
    "Imix", "Ik", "Akbal", "Kan", "Chicchan", "Cimi", "Manik", "Lamat", "Muluk",
    "Oc", "Chuen", "Eb", "Ben", "Ix", "Men", "Cib", "Caban", "Etznab", "Cauac", "Ahau"
]

mystic_titles = [
    "Volkov", "Popoca", "Mirztzin", "Xolotlzin", "Tepaneca", "Yuriev", "Ketzalin",
    "Yaretzin", "Nokturna", "Zaltzin", "Kaanbal", "Ixkalli"
]

def reduce_date(date_str):
    parts = date_str.split("-")
    total = sum(int(d) for d in "".join(parts))
    while total > 9999:
        total = sum(int(c) for c in str(total))
    return str(total).zfill(4)

def generate_signature(birth_date):
    seal = random.choice(mayan_seals)
    title = random.choice(mystic_titles)
    key = reduce_date(birth_date)
    signature = f"VortX{{{seal}.{title}:{title}#{key}}}"
    return signature

def guide():
    print("======================================")
    print("      VORTX SIGNATURE GENERATOR       ")
    print("======================================")
    print("Instructions:")
    print("- Enter your birth date in the format YYYY-MM-DD.")
    print("- The system will generate a unique symbolic signature.")
    print("- You must send your signature to: v0rt47@null.net")
    print("- If your signature is valid, you will gain access to the next phase.")
    print("")

def main():
    guide()
    birth_date = input("Enter birth date (YYYY-MM-DD): ")
    signature = generate_signature(birth_date)
    print("\nYour generated signature is:\n" + signature)
    input("\nPress ENTER to exit...")

if __name__ == "__main__":
    main()
