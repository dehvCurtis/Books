
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Model: {current_design.title()}')
        completed_models.append(current_design)

def show_completed_models(completed_models):
    for i in completed_models:
        print(f'Completed Models: {i.title()}')


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)