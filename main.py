from colorama import Fore, Style
from functions import set_variables, create_repos_folder, create_category, list_categories, create_repository, list_repositories, manage_categories

# Main function to orchestrate the process
def main():
    """
    Main function to orchestrate the repository creation process.
    """
    set_variables()
    create_repos_folder()

    while True:
        print(f"{Fore.YELLOW}Select an option:")
        print(f"{Fore.CYAN}1. Create Category")
        print("2. Create Repository")
        print("3. List Repositories")
        print("4. List Categories")
        print(f"5. Exit{Style.RESET_ALL}")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_category()
        elif choice == "2":
            create_repository()
        elif choice == "3":
            list_repositories()
        elif choice == "4":
            manage_categories()
        elif choice == "5":
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please enter a valid option.{Style.RESET_ALL}")

# Execute the main function
if __name__ == "__main__":
    main()
