import json
import os

METADATA_FILE="config.json"
CONFIG_DICT = None

def create_recipe(recipe_name, cuisine_type, ingredients):
    if not os.path.exists(CONFIG_DICT["main_folder"] + "/{}".format(cuisine_type)):
        os.makedirs(CONFIG_DICT["main_folder"] + "/{}".format(cuisine_type))

    with open(CONFIG_DICT["main_folder"] + "/{}/{}.txt".format(cuisine_type, recipe_name), 'w+') as f:
        f.write(ingredients)

def add_recipe():
    recipe_name = input("""Enter name of the recipe\n{}\n""".format("*" * 50))
    cuisine_type = input("""Enter type of cuisine like Indian, Arabian etc.\n{}\n""".format("*" * 50))
    total_portion = input("""Enter Total portion in mg\n{}\n""".format("*" * 50))
    ingredients = input("""Enter ingredients and amount in ingredient=amount(in mg) format. Each ingredient in a separate line\n{}\n""".format("*" * 50))
    ingredients += "\nTotal Portion={}".format(total_portion)
    create_recipe(recipe_name, cuisine_type, ingredients)

def list_recipes():
    pass

def text_file_path_to_dict(file_path):
    with open(file_path,'r') as f:
        text = f.read()

    if text:
        return {line.split("=")[0].strip():line.split("=")[1].strip() for line in text.split("\n") if line}

    return dict()

def print_recipe(recipe_path, recipe_name, file_path):
    with open(file_path,'r') as f:
        text = f.read()
    print("Cuisine Type: {}\nRecipe Name: {}\nIngredients: \n\n{}\n{}\n".format("-->".join(recipe_path), recipe_name, text, "*" * 50))

def filter_recipes():
    exclude_ingredients = input("""Enter ingredients that needs to be excluded from the recipe comma separated.\n{}\n""".format("*" * 50))
    include_ingredients = input("""Enter ingredients that needs to be included in the recipe comma separated.\n{}\n""".format("*" * 50))

    exclude_ingredients_list = [x.strip() for x in exclude_ingredients.split(",")]
    include_ingredients_list = [x.strip() for x in include_ingredients.split(",")]

    for root, dirs, files in os.walk("Main"):
        path = root.split(os.sep)
        for file in files:
            file_path = "/".join(path + [file])
            ingredient_dict = text_file_path_to_dict(file_path)

            if (any(x in ingredient_dict.keys() for x in include_ingredients_list) or not include_ingredients) and not any(x in ingredient_dict.keys() for x in exclude_ingredients_list):
                print_recipe(path[1:], file.split(".txt")[0], file_path)

            # print("-->".join(file_path[1:]))


def modify_recipe():
    pass

def get_config():
    with open(METADATA_FILE, 'r') as f:
        return json.load(f)

def main_function():
    global CONFIG_DICT

    CONFIG_DICT = get_config()
    options="""Enter an option from the below
    1. Add a recipe
    2. List recipes
    3. Filter recipes
    4. Modify total portion of a recipe
    {}
    """.format("*"*50)
    selected_option = input(options)
    print(selected_option)
    if selected_option == "1":
        add_recipe()
    elif selected_option == "2":
        list_recipes()
    elif selected_option == "3":
        filter_recipes()
    elif selected_option == "4":
        modify_recipe()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_function()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
