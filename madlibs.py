friendsName = input("Friends name: ")
hobby = input("What hobby you have: ")
wantToLook = input("How do you look thanks to hobby: ")
appearence = input("How you both look: ")
characterFeatures = input("Character features: ")

madlib = """Let me tell you about mv best friend. His name is {}. \
We have known each other for ages. We live in the same town and went \
to the same school. Now we study at the same university And though \
we study at different faculties, we see each other almost every day. \
My best friend is the first to come and support me in any difficult \
situation. We have a lot in common. We both do {} regularly. \
That's because we want to be {}. We really look \
very much alike. We have {}. 
We also have many similar features of character: we are \
{}.""".format(friendsName, hobby, wantToLook, appearence, characterFeatures)

print(madlib)