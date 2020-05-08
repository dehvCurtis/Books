
import printing_functions as prnt_func

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f'Model: {current_design.title()}')
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     for i in completed_models:
#         print(f'Completed Models: {i.title()}')

incomplete_designs = ['Tiger','Elephant','Gorilla']
complete_designs = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

prnt_func.print_models(incomplete_designs,complete_designs)
prnt_func.show_completed_models(complete_designs)