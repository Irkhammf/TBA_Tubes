import string
print('------------------------------------------------------------------------------------')
print('Selamat datang, silahkan lakukan chek validasi kata dengan menginputkan kata yang ada dalam daftar')
print('Berikut adalah daftar kata yang bisa dichek pada lexical analyzer ini: ')
print('ich, du, kleider, physik, saft, mais, studie, trinke, ernte, koche, nahen, tragen')
print('------------------------------------------------------------------------------------')
x = input()
x = str(x)
sentence = x
input_string = sentence.lower()+'#'

alphabet_list = list(string.ascii_lowercase)
state_list = ['q1','q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14'
, 'q15', 'q16','q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29'
, 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q40', 'q41']

transition_table = {}

for state in state_list:
  for alphabet in alphabet_list:
    transition_table[(state, alphabet)] = 'error'
  transition_table[(state, '#')] = 'error'
  transition_table[(state, ' ')] = 'error'

#spaces before input string
transition_table['q0', ' ']='q0'

#update the transition table for the following token: ich
transition_table[('q0', 'i')]= 'q1'
transition_table[('q1', 'c')]= 'q2'
transition_table[('q2', 'h')]= 'q40'
transition_table[('q40', ' ')]= 'q41'
transition_table[('q40', '#')]= 'accept'
transition_table[('q41', ' ')]= 'q41'
transition_table[('q41', '#')]= 'accept'

#transation for new token
transition_table[('q41', 'i')]= 'q1'
transition_table[('q41', 'e')]= 'q19'
transition_table[('q41', 'm')]= 'q9'
transition_table[('q41', 'd')]= 'q3'
transition_table[('q41', 't')]= 'q30'
transition_table[('q41', 'p')]= 'q4'
transition_table[('q41', 'k')]= 'q24'
transition_table[('q41', 's')]= 'q12'
transition_table[('q41', 'n')]= 'q35'

#update the transition table for the following token: du
transition_table[('q0', 'd')]= 'q3'
transition_table[('q3', 'u')]= 'q40'

#update the transition table for the following token: trinke
transition_table[('q0', 't')]= 'q30'
transition_table[('q30', 'r')]= 'q31'
transition_table[('q31', 'i')]= 'q32'
transition_table[('q32', 'n')]= 'q33'
transition_table[('q33', 'k')]= 'q18'
transition_table[('q18', 'e')]= 'q40'

#update the transition table for the following token: tragen
transition_table[('q31', 'a')]= 'q34'
transition_table[('q34', 'g')]= 'q37'

#update the transition table for the following token: physik
transition_table[('q0', 'p')]= 'q4'
transition_table[('q4', 'h')]= 'q5'
transition_table[('q5', 'y')]= 'q6'
transition_table[('q6', 's')]= 'q7'
transition_table[('q7', 'i')]= 'q8'
transition_table[('q8', 'k')]= 'q40'

#update the transition table for the following token: saft
transition_table[('q0', 's')]= 'q12'
transition_table[('q12', 'a')]= 'q13'
transition_table[('q13', 'f')]= 'q14'
transition_table[('q14', 't')]= 'q40'

#update the transition table for the following token: studie
transition_table[('q12', 't')]= 'q15'
transition_table[('q15', 'u')]= 'q16'
transition_table[('q16', 'd')]= 'q17'
transition_table[('q17', 'i')]= 'q18'
transition_table[('q18', 'e')]= 'q40'

#update the transition table for the following token: nahen
transition_table[('q0', 'n')]= 'q35'
transition_table[('q35', 'a')]= 'q36'
transition_table[('q36', 'h')]= 'q37'
transition_table[('q37', 'e')]= 'q38'
transition_table[('q38', 'n')]= 'q40'

#update the transition table for the following token: kleider
transition_table[('q0', 'k')]= 'q24'
transition_table[('q24', 'l')]= 'q25'
transition_table[('q25', 'e')]= 'q26'
transition_table[('q26', 'i')]= 'q27'
transition_table[('q27', 'd')]= 'q28'
transition_table[('q28', 'e')]= 'q29'
transition_table[('q29', 'r')]= 'q40'

#update the transition table for the following token: koche
transition_table[('q24', 'o')]= 'q22'
transition_table[('q22', 'c')]= 'q23'
transition_table[('q23', 'h')]= 'q18'
transition_table[('q18', 'e')]= 'q40'

#update the transition table for the following token: ernte
transition_table[('q0', 'e')]= 'q19'
transition_table[('q19', 'r')]= 'q20'
transition_table[('q20', 'n')]= 'q21'
transition_table[('q21', 't')]= 'q18'

#update the transition table for the following token: mais
transition_table[('q0', 'm')]= 'q9'
transition_table[('q9', 'a')]= 'q10'
transition_table[('q10', 'i')]= 'q11'
transition_table[('q11', 's')]= 'q40'

#lexical analysis
idx_char = 0
state = 'q0'
current_token = ' '
while state!='accept':
  current_char = input_string[idx_char]
  current_token += current_char
  state = transition_table[(state, current_char)]
  if state=='q40':
    print('current token: ', current_token, ', valid')
    current_token =' '
  if state == 'error':
    print('error')
    break;
  idx_char = idx_char + 1

#conclusion
if state == 'accept':
  print('semua token di input: ', sentence, ', valid')
