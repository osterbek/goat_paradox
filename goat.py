import random

if __name__ == '__main__':
    counter_wins = [0, 0, 0]
    for game in range(1, 1001):
        print("\nGame {}".format(game))
        winner_gate = random.randint(0, 2)
        selected_gate = random.randint(0, 2)
        presented_empty_gate = (selected_gate + 1) % 3
        if winner_gate == presented_empty_gate:
            presented_empty_gate = (presented_empty_gate + 1) % 3
        gates = [0, 1, 2]
        gates.remove(selected_gate)
        gates.remove(presented_empty_gate)
        third_gate = gates[0]
        strategy = ['Remain Gate', 'Fifty-Fifty', 'Change Gate']
        choice = [selected_gate, random.choice([selected_gate, third_gate]), third_gate]
        print(" Random winner gate: {}".format(winner_gate))
        print("    Random selected gate: {}".format(selected_gate))
        print("    Empty presented gate: {}".format(presented_empty_gate))
        print("    Third gate:           {}".format(third_gate))
        for idx, gate in enumerate(choice):
            counter_wins[idx] += (gate == winner_gate)
            print("       Strategy " + strategy[idx] + ": {} => Win={}".format(gate, gate == winner_gate))
            print("         Total wins: {}/{} = {:.3f} ".format(counter_wins[idx], game, counter_wins[idx] / game))
