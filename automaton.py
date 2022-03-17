class Automaton():

    def __init__(self, config_file):
        self.config_file = config_file
        print("Hi, I'm an automaton!")

    def validate(self):
        """Return a Boolean

        Returns true if the config file is valid,
        and raises a ValidationException if the config is invalid.
        """
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
                return 0
                check = 0
            if transition[1] not in Sigma: 
                return 0
                check = 0

            if transition[2] not in States: 
                return 0
                check = 0

        if check == 1 : 
            return 1

        return "I can't tell if the config file is valid... yet!"

    def accepts_input(self, input_str):
        """Return a Boolean

        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):
        """Return the automaton's final configuration
        
        If the input is rejected, the method raises a
        RejectionException.
        """
        pass
    

if __name__ == "__main__":
    a = Automaton('your_config_file')
    print(a.validate())
