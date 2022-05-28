def outer_function(some_local_name):
    def inner_function(other_local_name):
         # Tiene acceso a la built-in function print y al nombre local some_local_name
         print(some_local_name) 
        
         # También tiene acceso a su scope local
         print(other_local_name)
         

some_var_in_other_scope = 10

def some_function():
    global some_var_in_other_scope

    Some_var_in_other_scope += 1