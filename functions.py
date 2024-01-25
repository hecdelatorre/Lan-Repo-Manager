import os
import subprocess
import json

# Initialize global variables with default values
parent_folder = ""
ip_or_hostname = ""
user = ""
folder_name = ""

# Function to set up variables
def set_variables():
    """
    Set up global variables by loading values from the 'env_variables.json' file.
    """
    global parent_folder, ip_or_hostname, user, folder_name
    env_file_path = os.path.join(os.path.dirname(__file__), "env_variables.json")

    with open(env_file_path, "r") as env_file:
        env_variables = json.load(env_file)

    parent_folder = env_variables.get("PARENT_FOLDER", "")
    ip_or_hostname = env_variables.get("IP_OR_HOSTNAME", "")
    user = env_variables.get("USER", "")
    folder_name = env_variables.get("FOLDER_NAME", "")

# Function to create the 'Repos' folder if it doesn't exist
def create_repos_folder():
    """
    Create the 'Repos' folder if it doesn't exist.
    """
    if not os.path.exists(os.path.join(parent_folder, folder_name)):
        os.makedirs(os.path.join(parent_folder, folder_name))

# Function to create a category folder
def create_category():
    """
    Create a category folder based on user input.
    """
    print("Existing Categories:")
    list_categories()
    print()

    while True:
        category_name = input("Enter the name of the project category: ")

        # Validate category name
        if "-" not in category_name:
            category_name = category_name.lower().replace(" ", "-")

            category_path = os.path.join(parent_folder, folder_name, category_name)

            if not os.path.exists(category_path):
                os.makedirs(category_path)
                print(f"Category folder '{category_name}' created successfully.")
                break
            else:
                print(f"Category folder '{category_name}' already exists. Choose a different category name.")
        else:
            print("Invalid category name. Please avoid using hyphens.")

# Function to list categories
def list_categories(show_number=False):
    """
    List existing categories.
    """
    categories = [os.path.basename(path) for path in os.listdir(os.path.join(parent_folder, folder_name))]
    for i, category in enumerate(categories, start=1):
        if show_number:
            print(f"{i}. {category}")
        else:
            print(category)
    return categories

# Function to create a project folder and initialize a bare Git repository
def create_repository():
    """
    Create a project folder and initialize a bare Git repository based on user input.
    """
    categories = [os.path.join(parent_folder, folder_name, category) for category in os.listdir(os.path.join(parent_folder, folder_name))]
    if not categories:
        print("No categories found. Please create a category first.")
        return

    print("Select a category to create the project:")
    list_categories(show_number=True)
    print()

    while True:
        category_number = input("Enter category number: ")

        if category_number.isdigit():
            index = int(category_number) - 1
            if 0 <= index < len(categories):
                selected_category = categories[index]

                project_name = input("Enter the name of the project: ")

                # Validate project name
                if "-" not in project_name:
                    project_name = project_name.lower().replace(" ", "-")

                    category_name = os.path.basename(selected_category)
                    project_path = os.path.join(selected_category, f"{project_name}.git")

                    if not os.path.exists(project_path):
                        os.makedirs(project_path)
                        print(f"Project folder '{project_name}' created successfully.")

                        # Initialize a bare Git repository
                        subprocess.run(["git", "init", "--bare", project_path])

                        # Print repository address on the local network
                        print(f"Repository address on local network: {user}@{ip_or_hostname}:{project_path}")

                        break
                    else:
                        print(f"Project folder '{project_name}' already exists in the selected category. Choose a different project name.")
                else:
                    print("Invalid project name. Please avoid using hyphens.")
            else:
                print("Invalid category number. Please enter a valid number.")
        else:
            print("Invalid input. Please enter a valid number.")

# Function to list repositories
def list_repositories():
    """
    List repositories in a selected category.
    """
    print("Select a category to list repositories (press 'B' to go back):")
    categories = list_categories(show_number=True)
    print()

    category_number = input("Enter category number: ")
    if category_number.lower() == "b":
        return

    if category_number.isdigit():
        index = int(category_number) - 1
        if 0 <= index < len(categories):
            selected_category = categories[index]
            repositories = [repo[:-4] for repo in os.listdir(os.path.join(parent_folder, folder_name, selected_category)) if repo.endswith('.git')]

            print("\nRepositories of the selected category:")
            for i, repo in enumerate(repositories, start=1):
                print(f"{i}. {repo} - {user}@{ip_or_hostname}:{os.path.join(parent_folder, folder_name, selected_category, repo)}.git")

            while True:
                repo_number = input("Enter repository number (press 'B' to go back): ")
                if repo_number.lower() == "b":
                    return

                if repo_number.isdigit():
                    repo_index = int(repo_number) - 1
                    if 0 <= repo_index < len(repositories):
                        selected_repo = repositories[repo_index]

                        print(f"\nOptions for the selected repository '{selected_repo}':")
                        print("1. Rename Repository")
                        print("2. Delete Repository")
                        print("3. Go Back")

                        option = input("Enter your choice: ")
                        if option == "1":
                            rename_repository(selected_category, selected_repo)
                        elif option == "2":
                            delete_repository(selected_category, selected_repo)
                        elif option == "3":
                            break
                        else:
                            print("Invalid choice. Please enter a valid option.")
                    else:
                        print("Invalid repository number. Please enter a valid number.")
                else:
                    print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid category number. Please enter a valid number.")
    else:
        print("Invalid input. Please enter a valid number.")

# Function to rename a repository
def rename_repository(category, old_repo):
    """
    Rename a repository based on user input.
    """
    print(f"Rename Repository '{old_repo}':")
    new_repo = input("Enter the new name for the repository: ")

    if "-" not in new_repo:
        new_repo = new_repo.lower().replace(" ", "-")
        old_path = os.path.join(parent_folder, folder_name, category, f"{old_repo}.git")
        new_path = os.path.join(parent_folder, folder_name, category, f"{new_repo}.git")

        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"Repository '{old_repo}' has been renamed to '{new_repo}' successfully.")
        else:
            print(f"Repository '{old_repo}' not found.")
    else:
        print("Invalid repository name. Please avoid using hyphens.")

# Function to delete a repository
def delete_repository(category, repository):
    """
    Delete a repository based on user input.
    """
    print(f"Delete Repository '{repository}':")
    confirmation = input(f"Type 'i-am-sure' to delete the repository '{repository}' along with its folder: ")

    if confirmation.lower() == "i-am-sure":
        repository_path = os.path.join(parent_folder, folder_name, category, f"{repository}.git")
        if os.path.exists(repository_path):
            import shutil
            shutil.rmtree(repository_path)
            print(f"Repository '{repository}' has been deleted successfully.")
        else:
            print(f"Repository '{repository}' not found.")
    else:
        print("Deletion aborted.")

# Function to manage categories
def manage_categories():
    """
    Manage categories by listing and providing options to rename or delete.
    """
    print("Select a category to manage (press 'B' to go back):")
    categories = list_categories(show_number=True)
    print()

    category_number = input("Enter category number: ")
    if category_number.lower() == "b":
        return

    if category_number.isdigit():
        index = int(category_number) - 1
        if 0 <= index < len(categories):
            selected_category = categories[index]
            print("\nOptions for the selected category:")
            print("1. Rename Category")
            print("2. Delete Category")
            print("3. Go Back")

            option = input("Enter your choice: ")
            if option == "1":
                rename_category(selected_category)
            elif option == "2":
                delete_category(selected_category)
            elif option == "3":
                pass
            else:
                print("Invalid choice. Please enter a valid option.")
        else:
            print("Invalid category number. Please enter a valid number.")
    else:
        print("Invalid input. Please enter a valid number.")

# Function to rename a category
def rename_category(old_category):
    """
    Rename a category based on user input.
    """
    print(f"Rename Category '{old_category}':")
    new_category = input("Enter the new name for the category: ")

    if "-" not in new_category:
        new_category = new_category.lower().replace(" ", "-")
        old_path = os.path.join(parent_folder, folder_name, old_category)
        new_path = os.path.join(parent_folder, folder_name, new_category)

        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"Category '{old_category}' has been renamed to '{new_category}' successfully.")
        else:
            print(f"Category '{old_category}' not found.")
    else:
        print("Invalid category name. Please avoid using hyphens.")

# Function to delete a category
def delete_category(category):
    """
    Delete a category based on user input.
    """
    print(f"Delete Category '{category}':")
    confirmation = input(f"Type 'i-am-sure' to delete the category '{category}' along with its contents: ")

    if confirmation.lower() == "i-am-sure":
        category_path = os.path.join(parent_folder, folder_name, category)
        if os.path.exists(category_path):
            import shutil
            shutil.rmtree(category_path)
            print(f"Category '{category}' has been deleted successfully.")
        else:
            print(f"Category '{category}' not found.")
    else:
        print("Deletion aborted.")
