def badge_maker(name):
    return "Hello, my name is {}.".format(name)


def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges


def assign_rooms(speakers):
    room_assignments = []
    for index, speaker in enumerate(speakers):
        room_assignments.append("Hello, {}! You'll be assigned to room {}!".format(speaker, index+1))
    return room_assignments

def printer(speakers):
    badges = batch_badge_creator(speakers)
    room_assignments = assign_rooms(speakers)

    for badge in badges:
        print(badge)
    
    for room_assignment in room_assignments:
        print(room_assignment)


printer (["Arel", "Carol"])
