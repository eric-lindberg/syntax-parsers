'''
Created on Feb 22, 2020

@author: Eric Lindberg
'''
import nltk

class SyntaxMain:
    def __init__(self):
        self.parser = None
        self.done = False
    
    def handle_input(self, cmd_str):
        cmd = cmd_str.lower().strip()
        if not cmd:
            return
        
        if cmd.startswith('#'):
            self.perform_command(cmd[1:].strip())
        elif self.parser:
            try:
                sentence = cmd.split()
                for tree in self.parser.parse(sentence):
                    print(tree)
            except Exception as e:
                print('Error reading sentence')
                print(e)
        else:
            print('No parser available for that sentence')
            self.print_error()
            
    def print_error(self, cmd_str = None):
        if cmd_str:
            print('Unrecognized command "' + cmd_str + '"')
        print('#help for help')
        
    def perform_command(self, cmd_str):
        if cmd_str == 'help':
            print('#help -- print this list of commands')
            print('#exit -- end this program')
            print('#load <filename> -- load parser using specified grammar file')
            print('Any other string -- intepreted as a sentence to be parsed')
        elif cmd_str == 'exit':
            self.done = True
        elif cmd_str.split()[0] == 'load':
            try:
                self.parser = nltk.load_parser(cmd_str.split()[1], trace=2)
            except Exception as e:
                print('Error reading grammar "' + cmd_str.split()[1] + '"')
                print(e)
                return
            print('Parser with grammar "' + cmd_str.split()[1] + '" successfully loaded')
        else:
            print_error(cmd_str)
            

if __name__ == '__main__':
    print('#help for help')
    print('#exit to end')
    
    controller = SyntaxMain()
    
    while not controller.done:
        cmd_str = input('> ')
        
        controller.handle_input(cmd_str)