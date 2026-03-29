from salon_post_generator import SalonPostGenerator

generator = SalonPostGenerator()

print("🌟 Daily Salon Post Helper for the Salon 🌟\n")

while True:
    print("Would you like a:")
    print("1. Random post")
    print("2. Post by category (haircut, color, blowout, general)")
    print("3. Quit")

    choice = input("\nType 1, 2, or 3: ").strip()

    if choice == "1":
        print("\nHere's your random post idea:")
        print(generator.generate_daily_post())   # ← Use generate_daily_post, not get_random_post

    elif choice == "2":
        category = input("Which category? (haircut / color / blowout / general): ").strip().lower()
        post = generator.generate_daily_post()
        print("\nHere's your post idea:")
        print(post)

    elif choice == "3":
        print("\nHave a great day! 💇‍♀️")
        break
    else:
        print("❌ Please type 1, 2, or 3.\n")