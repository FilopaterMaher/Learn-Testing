from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Felopater Maher' work??"""
    formatted_name = get_formatted_name('felopater', 'maher')
    assert formatted_name == "Felopater Maher"
    

def test_first_middle_last_name():
    """Do names like 'Felopater Maher Faris' work??"""
    formatted_name = get_formatted_name('felopater','faris' , 'maher')
    assert formatted_name == "Felopater Maher Faris" 