def read_input(file_name):
    try:
        with open(file_name, "r") as file:
            first_line = file.readline().split()
            if not first_line:
                print("File was empty.")
                raise IOError
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
    except FileNotFoundError:
        print("File not found or cannot be opened.")
        return None


def write_output(file_name, num_beers):
    with open(file_name, "w") as file:
        file.write(str(num_beers))


def find_min_beer_coverage(N, B, preferences):
    set_cover = []
    uncovered = set(range(B))

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
