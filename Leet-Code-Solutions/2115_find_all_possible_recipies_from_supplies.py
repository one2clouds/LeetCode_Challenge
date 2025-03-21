
# for each recipe call dfs function in 3rd last line. inside vfs, if the recipe has been visited or not in our recipues then return false and exit, 
# if it isn't then add the recipe in visited set, then iterate through every ingredient of the recipe and check if they are in supply, and even if
#  they are not in dfs(ing), i.e recursion to make that item first, if it isn't made. If ingredient isn't in supply and visited, return false and exit, 
# but else case then, the ingredient is available and we can make that recipe, so we append the recipe in result as well as supplies

def findAllRecipes(recipes, ingredients, supplies):
        adj = {} # hashmap of recipe and their corresponding ingredients needed 
        visited = set()
        supplies = set(supplies)
        result = []


        for i, recipe in enumerate(recipes):
            adj[recipe] = ingredients[i]
        
        def dfs(recipe):
            if recipe in visited or recipe not in recipes:
                return False
            
            visited.add(recipe)
            for ing in adj[recipe]:
                if ing not in supplies and not dfs(ing):
                    return False
            result.append(recipe)
            supplies.add(recipe)
            return True
        
        for recipe in recipes:
            dfs(recipe)
        return result


if __name__== "__main__":
    recipes = ["bread"]
    ingredients = [["yeast","flour"]]
    supplies = ["yeast","flour","corn"]
    print(findAllRecipes(recipes, ingredients, supplies))

    recipes = ["bread","sandwich"]
    ingredients = [["yeast","flour"],["bread","meat"]]
    supplies = ["yeast","flour","meat"]
    print(findAllRecipes(recipes, ingredients, supplies))

    
    recipes = ["bread","sandwich","burger"]
    ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
    supplies = ["yeast","flour","meat"]
    print(findAllRecipes(recipes, ingredients, supplies))
