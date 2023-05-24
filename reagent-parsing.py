# ini w/ a dict.
procedure  = {'reagents':['NaH', 'tBuOK', 'MeOH' ]}
set_up_text = ''
for reagent in procedure['reagents'][:-2]:
    set_up_text += 