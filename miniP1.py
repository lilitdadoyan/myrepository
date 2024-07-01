def get_inputs(placeholder_list):
    user_inputs = {}
    for placeholder in placeholder_list:
        user_input = input(f"Please type a {placeholder}: ")
        user_inputs[placeholder] = user_input
    return user_inputs


def generate_story(template, user_inputs):
    for placeholder, user_input in user_inputs.items():
        template = template.replace(f"({placeholder})", user_input)
    return template


def main():
    templates = [
        "It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation). "
        "The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who "
        "have (Color) (Part of the Body). If someone wants to come into my room I told them that they have to (Verb) "
        "first. I've decorated my room with (Number2) (Noun2). Today I talked to a doctor and they were wearing a "
        "(Noun3) on their (Part of the Body2). I heard that all doctors (Verb2) (Noun4) every day for breakfast. The most "
        "(Adjective3) thing about being in the hospital is the (Silly Word) (Noun5)!",

        "This weekend I am going camping with (Proper Noun (Person's Name)). I packed my lantern, sleeping bag, "
        "and (Noun). I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective (Feeling) 2) we might see a(n) "
        "(Animal), I hear they're kind of dangerous. While we're camping, we are going to hike, fish, and (Verb2). I "
        "have heard that the (Color) lake is great for (Verb (ending in ing)). Then we will (Adverb (ending in ly)) hike "
        "through the forest for (Number) (Measure of Time). If I see a (Color) (Animal) while hiking, I am going to bring "
        "it home as a pet! At night we will tell (Number2) (Silly Word) stories and roast (Noun2) around the campfire!!",

        "Dear (Proper Noun (Person's Name)), I am writing to you from a (Adjective) castle in an enchanted forest. I "
        "found myself here one day after going for a ride on a (Color) (Animal) in (Place). There are (Adjective2) "
        "(Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here! In the (Room in a House) there is a pool full "
        "of (Noun). I fall asleep each night on a (Noun2) of (Noun (Plural)3) and dream of (Adjective4) (Noun (Plural)4). It "
        "feels as though I have lived here for (Number) (Measure of time). I hope one day you can visit, although the "
        "only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!"
    ]

    placeholders_list = [
        ["Number", "Measure of time", "Mode of Transportation", "Adjective", "Adjective2", "Noun", "Color",
         "Part of the Body",
         "Verb", "Number2", "Noun2", "Noun3", "Part of the Body2", "Verb2", "Noun4", "Adjective3", "Silly Word",
         "Noun5"],

        ["Proper Noun (Person's Name)", "Noun", "Adjective (Feeling)", "Verb", "Adjective (Feeling) 2", "Animal",
         "Verb2",
         "Color", "Verb (ending in ing)", "Adverb (ending in ly)", "Number", "Measure of Time", "Color", "Animal",
         "Number2", "Silly Word", "Noun2"],

        ["Proper Noun (Person's Name)", "Adjective", "Color", "Animal", "Place", "Adjective2",
         "Magical Creature (Plural)",
         "Adjective3", "Magical Creature (Plural)2", "Room in a House", "Noun", "Noun2", "Noun (Plural)3", "Adjective4",
         "Noun (Plural)4", "Number", "Measure of time", "Verb (ending in ing)", "Adjective5", "Noun5"]
    ]

    print("Choose a story template:")
    for i, template in enumerate(templates, 1):
        print(f"{i}. Template {i}")

    choice = int(input("Enter the number of the template you want to use: ")) - 1
    selected_template = templates[choice]
    selected_placeholders = placeholders_list[choice]

    user_inputs = get_inputs(selected_placeholders)
    story = generate_story(selected_template, user_inputs)

    print("\nHere is your story:\n")
    print(story)


if __name__ == "__main__":
    main()
