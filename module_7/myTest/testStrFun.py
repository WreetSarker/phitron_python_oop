import textFuncs

s = "i love bangladesh"


def test_script():
        ret1 = textFuncs.make_upper(s)
        ret2 = textFuncs.make_lower(s)
        ret3 = textFuncs.make_capital(s)

        
        assert "I LOVE BANGLADESH"==ret1 and  "i love bangladesh" == ret2 and  s.capitalize() == ret3

    
        
        

    
        
        