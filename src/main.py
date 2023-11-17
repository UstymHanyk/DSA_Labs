def read_input(file_name):
    with open(file_name, "r") as file:
        first_line = file.readline().split()
        N = int(first_line[0])  # Number of employees
        B = int(first_line[1])  # Number of beers
        preferences = []
        beer_preferences = file.readline().strip().split()
        for beer_preference in beer_preferences:
            preference = []
            for i in range(B):
                if beer_preference[i] == "Y":
                    preference.append(i)
            preferences.append(preference)
    return N, B, preferences


def write_output(file_name, num_beers):
    with open(file_name, "w") as file:
        file.write(str(num_beers))


def find_min_beer_coverage(N, B, preferences):
    elements = set(range(B))
    set_cover = []
    uncovered = elements.copy()

    while uncovered:
        best_subset = set()
        best_score = 0
        best_index = -1

        for index, subset in enumerate(preferences):
            score = len(set(subset) & uncovered)

            if score > best_score:
                best_subset = subset
                best_score = score
                best_index = index

        if best_score == 0:
            break

        set_cover.append(list(best_subset))
        uncovered -= set(best_subset)
        del preferences[best_index]
    return len(set_cover)


if __name__ == "__main__":
    input_file = "../test/input.txt"
    output_file = "../test/output.txt"

    n, b, preferences = read_input(input_file)
    num_beers = find_min_beer_coverage(n, b, preferences)
    write_output(output_file, num_beers)
