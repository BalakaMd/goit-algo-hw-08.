import heapq


def minimize_cost(cables):
    """
    A function to minimize the cost of cables by combining the shortest cables until only one remains.
    """
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        # Беремо два найкоротших кабелі та об'єднуємо їх
        shortest1 = heapq.heappop(cables)
        shortest2 = heapq.heappop(cables)
        connection_cost = shortest1 + shortest2
        total_cost += connection_cost

        # Додаємо новий кабель до піраміди
        heapq.heappush(cables, connection_cost)

    return total_cost


cables_list = [4, 8, 6, 12]
min_cost = minimize_cost(cables_list)
print("Мінімальні витрати:", min_cost)
