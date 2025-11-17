from pyscript import display 

Basketball_Varsity = {'Shinothebest', 'Asheley', 'Rosemary', 'Axel', 'Grisha'}
Communication_Arts  = {'Shinothebest', 'Grahambell','Grisha','Akiridion', 'Tophan'}
check_Bball = 'Shino'

display(Basketball_Varsity, target = 'output3')

display(Basketball_Varsity, Communication_Arts, target = 'output')

display(Basketball_Varsity & Communication_Arts, target = 'output2')

display(Communication_Arts, target = 'output4')

display(Basketball_Varsity.symmetric_difference(Communication_Arts), target = 'output5')
