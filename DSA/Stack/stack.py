# A Stack is a data structure that follows LIFO — Last In, First Out.
# Used in Real Application
#**Example:**
#A stack of plates — the last plate placed on top is the first plate removed.

# Push = Add
# Pop = Remove
# Peek = See top


# 📱 Mobile app screen navigation
#  🌐 Browser Back button
# ↩️ Undo/Redo in editors
# 🧮 Calculator/expression evaluation
# 🔄 Function calls in programs
# 🔁 Recursion
# 🧭 DFS in graphs
# 🎮 Game backtracking
# 💻 Compiler syntax checking
# 📝 Text editor history

stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("stack", stack)

print("Top:", stack[-1])
deleted = stack.pop()

print("Deleted: ", deleted)
print("Stack:", stack)




