careers = ["football player", "actor", "author", "singer"]
i = careers.index("football player")
print("football player" in careers)
careers.append("doctor")
careers.insert(0, "dog walker")
for job in careers:
    print(job)