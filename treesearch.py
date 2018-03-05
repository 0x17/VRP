import instance


def full_enumeration(inst: instance.Instance):
    def tour_length(tour):
        return sum([inst.cij[i][j] for (i, j) in [0] + tour + [0]])

    def recursive_helper(partial_solution, current_tour, remaining_locations):
        if not remaining_locations: return partial_solution

        # if tour_length(partial_solution[current_tour]) > inst.b: return recursive_helper(partial_solution, current_tour+1, remaining_locations)

        for remaining_location in remaining_locations:
            updated_tour = partial_solution[current_tour].copy()
            updated_tour.append(remaining_location)
            npartial_solution = partial_solution.copy()
            if tour_length(updated_tour) <= inst.b:
                npartial_solution[current_tour] = updated_tour
            else:
                current_tour += 1
                npartial_solution[current_tour] = [remaining_location]
            return recursive_helper(npartial_solution, current_tour, remaining_locations.copy().remove(remaining_location))

    recursive_helper([[] for m in inst.M], 0, inst.I[1:])
