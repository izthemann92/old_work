# Blake Mann
# PSID: 1832387
class FoodItem:
    def __init__(self, name = "None", fat = 0.0, carbs = 0.0, protien = 0.0, servings = 0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protien
        self.servings = servings

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
# MyInstance = FoodItem()
# MyInstance.print_info()

if __name__ == "__main__":

    food1 = FoodItem()
    name = input()
    fat = float(input())
    carbs = float(input())
    protein = float(input())

    food2 = FoodItem(name, fat, carbs, protein)

    num_servings = float(input())

    food1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food1.get_calories(num_servings)))

    print()

    food2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food2.get_calories(num_servings)))


