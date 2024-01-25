from functions import set_variables, create_repos_folder, create_category, list_categories, create_repository, list_repositories, manage_categories

# Main function to orchestrate the process
def main():
    """
    Main function to orchestrate the repository creation process.
    """
    set_variables()
    create_repos_folder()

    while True:
        print("Select an option:")
        print("1. Create Category")
        print("2. Create Repository")
        print("3. List Repositories")
        print("4. List Categories")
        print("5. Exit")

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
            print("Invalid choice. Please enter a valid option.")

# Execute the main function
if __name__ == "__main__":
    main()
