import os
import json
import subprocess

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
def list_categories():
    """
    List existing categories.
    """
    categories = [os.path.basename(path) for path in os.listdir(os.path.join(parent_folder, folder_name))]
    for i, category in enumerate(categories, start=1):
        print(f"{i} {category}")

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
    list_categories()
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

# Function to list repositories in a category
def list_repositories():
    """
    List repositories in a selected category.
    """
    print("Select a category to list repositories:")
    list_categories()
    print()

    while True:
        category_number = input("Enter category number: ")

        if category_number.isdigit():
            index = int(category_number) - 1
            categories = [os.path.join(parent_folder, folder_name, category) for category in os.listdir(os.path.join(parent_folder, folder_name))]
            if 0 <= index < len(categories):
                selected_category = categories[index]

                repositories = [f"{user}@{ip_or_hostname}:{os.path.join(selected_category, repo)}" for repo in os.listdir(selected_category) if repo.endswith('.git')]

                if repositories:
                    print("Repositories in the selected category:")
                    for repo in repositories:
                        print(repo)
                else:
                    print("No repositories found in the selected category.")
                break
            else:
                print("Invalid category number. Please enter a valid number.")
        else:
            print("Invalid input. Please enter a valid number.")
