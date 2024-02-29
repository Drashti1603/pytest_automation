import pytest
from Keyword.test_on_usr_def_key import SearchPage, FilterPage, SelectPage, CartPage, Login 
from Config.config import session

def test_Flipkart(session):
    ##--SEARCH--##
    SearchPage(session).test_searching()

    ##--FILTER--##
    FilterPage(session).test_filter()

    ##--SELECT--##
    SelectPage(session).test_selecting()

    ##--CART--##
    CartPage(session).test_cart_and_login()

    ##--FAIL--##
    Login(session).login()    
