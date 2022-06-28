stack = []

#pushing using append()
stack.append(1)
stack.append(2)
stack.append(3)
print("After pushing: ", stack)

#pop using pop()
stack.pop()
print("After popping: ", stack)

#check if stack empty
#|if stack| returns true if not empty, false if empty|
if stack:
    print("Not empty")
else:
    print("Empty")

#size of stack
print("stack size: ", len(stack))

#get stack top
print("Stack top: ", stack[-1])

