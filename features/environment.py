# def before_step(context, step):
#     print("*************** before_step")
#
#
# def after_step(context, step):
#     print("*************** after_step")
#     print("")
#
#
def before_scenario(context, scenario):
    print("")
    print("****************************** before_scenario")


def after_scenario(context, scenario):
    print("****************************** after_scenario")
    print("")

# def before_scenario(context, scenario):
#     print("")
#     print("*************** before_scenario")
#
#
# def after_scenario(context, scenario):
#     if "BVT" in scenario.tags:
#         print("Executes only for Scenarios tagged as - BVT")
#     else:
#         print("Executes for Scenarios expect BVT")
#
#     print("*************** after_scenario")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
