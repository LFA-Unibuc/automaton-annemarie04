f = open("data.txt", "r")

Sigma = set()
States = set()
Transitions = []
final_states = set()

ok = 0

for line in f.readlines() :
    if line.startswith('#') : 
        continue

    if line.startswith('Sigma') :
        ok = 1
        continue
    
    if line.startswith('States') :
        continue

    if line.startswith('Transitions') :
        continue

    if line.startswith('End') :
        ok += 1
        continue

    if ok == 1 :
        Sigma.add(line.strip())
    
    if ok == 2 :
        if len(line.strip().split(',')) > 2 :
            States.add(line.strip().split()[0])

            if line.strip().split(',')[1] == 'F' :
                final_states.add(line.strip().split(' ,')[0])

            if line.strip().split(',')[1] == 'S' :
                initial_state = line.strip().split(' ,')[0]

            if line.strip().split(',')[2] == 'F' :
                final_states.add(line.strip().split(' ,')[0])

            if line.strip().split(',')[2] == 'S' :
                initial_state = line.strip().split(' ,')[0]

        elif len(line.strip().split(',')) == 2 :
            States.add(line.strip().split()[0])

            if line.strip().split(',')[1] == 'F' :
                final_states.add(line.strip().split(' ,')[0])

            if line.strip().split(',')[1] == 'S' :
                initial_state = line.strip().split(' ,')[0]

        else:
            States.add(line.strip())

    if ok == 3 :
        Transitions.append(tuple(x for x in line.strip().split(", ")))

check = 1

for transition in Transitions :
    if transition[0] not in States: 
        print("EROARE!")
        check = 0
    if transition[1] not in Sigma: 
        print("EROARE!")
        check = 0

    if transition[2] not in States: 
        print("EROARE!")
        check = 0

if check == 1 :
    print("EVERYTHING OK")

# print(Sigma)
# print(States)
# print(Transitions)
# print(final_states)
# print(initial_state)

