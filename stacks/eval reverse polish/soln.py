class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # num stack [ 3 3 ]
        # + -> pop + pop = 3 add 3 to the stack
        #return pop
        numStack = []
        for i in range(len(tokens)):
            if (tokens[i] in ['+', '-', '*', '/']):
                arg1 = numStack.pop()
                arg2 = numStack.pop()
                print(numStack)
                print(arg1, arg2)
                if (tokens[i] == '+'):
                    numStack.append(arg2 + arg1)
                elif (tokens[i] == '-'):
                    numStack.append(arg2 - arg1)
                elif (tokens[i] == '*'):
                    numStack.append(arg2 * arg1)
                else:
                    numStack.append(int(arg2 / arg1))
            else:
                numStack.append(int(tokens[i]))
            
        return numStack.pop()
