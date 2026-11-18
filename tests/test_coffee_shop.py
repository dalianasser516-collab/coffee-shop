from shop import Coffee_shop , Branch1 , Branch2 , is_payment_sufficient
def test_show_menu():
    menu = ["mocha","matcha"]
    branch = Coffee_shop(menu,500,9.5)
    result= branch.show_menu()
    assert result == menu

def test_show_menu_empty():
    menu =[]
    branch = Coffee_shop([],500,9.5)
    result= branch.show_menu()
    assert result == menu

def test_branch1_minimum_charge():
    assert Branch1.minimum_charge == 500

def test_branch2_minimum_charge():
    assert Branch2.minimum_charge == 700

def test_branch1_rating():
    assert Branch1.rating == 10

def test_branch2_rating():
    assert Branch2.rating == 8.6

def test_branch1_menu():
    assert Branch1.menu == ['iced spanish latte', 'matcha', 'mocha', 'cakes', 'cheese cakes']

def test_branch2_menu():
    assert Branch2.menu == ['iced spanish latte', 'matcha', 'salted caramel', 'cakes', 'fresh juices']

def test_branch1_str():
    assert str(Branch1) == "['iced spanish latte', 'matcha', 'mocha', 'cakes', 'cheese cakes'],500,10"

def test_branch2_str():
    assert str(Branch2) == "['iced spanish latte', 'matcha', 'salted caramel', 'cakes', 'fresh juices'],700,8.6"

def test_branch1_eq_branch2():
    assert (Branch1 == Branch2) == False

def test_branch1_lt_branch2():
    assert (Branch1 < Branch2) == False

def test_branch2_lt_branch1():
    assert (Branch2 < Branch1) == True

def test_is_good_place_true():
    assert Coffee_shop.is_good_place(9.5) == True

def test_is_good_place_false():
    assert Coffee_shop.is_good_place(8.0) == False

def test_special_offers():
    special_offer_branch = Coffee_shop.special_offers()
    assert special_offer_branch.menu == ['two iced spanish latte', 'two cheese cakes']
    assert special_offer_branch.minimum_charge == 400
    assert special_offer_branch.rating == 9.8

def test_is_payment_sufficient_true():
    assert is_payment_sufficient(600, 500) == True

def test_is_payment_sufficient_false():
    assert is_payment_sufficient(400, 500) == False